.. _gridftp:

=======
GridFTP
=======

The `GridFTP protocol <https://wickie.hlrs.de/platforms/index.php/Data_Transfer_with_GridFTP>`_ can be used for high-performance data transfer. Alternative, more extensive guide can be found `here <https://wickie.hlrs.de/dgrid/>`_.
In order to use it, a lot of 'paperwork' has to be done.

Prequisites:

- A X.509 certificate
- The globus client

-----------------
X.509 certificate
-----------------

You need a certifiacte to use the service. To get a certificate issue a request over this `webinterface <https://pki.pca.dfn.de/grid-root-ca/cgi-bin/pub/pki?cmd=basic_csr;id=1;menu_item=1&RA_ID=123>`_.
During the procedure of applying for a certificate you will be requested to print out a form and show up at the Grid Registrierungsstelle (RA) and show your passport to identify yourself. If you have already a grid certificate and want to extend it, make sure you fill in the fields exactly the same as in your existing certificate (otherwise a new account will be created).

You will then receive an email with the link to import your certificate. Use a browser like Firefox to import the certificate. It should be on the same machine that issued the request.
In Firefox export your certificate and save it somewhere on your disk.
Next step is to extract the certificate and keyfile. You have to enter the password you chose when saving the file in firefox::

   Extract the private key (userkey.pem)
   user@host:~> openssl pkcs12 -in GermanGridCert.p12 -out userkey.pem -nocerts
   Enter Import Password: ********
   MAC verified OK
   Enter PEM pass phrase: ********
   Verifying - Enter PEM pass phrase: ********
   user@host:~>

   Extract the user certificate (usercert.pem)
   user@host:~> openssl pkcs12 -in GermanGridCert.p12 -out usercert.pem -clcerts -nokeys
   Enter Import Password: ********
   MAC verified OK
   user@host:~>

The before created files containing user certificate and private key have to be moved to the folder ~./globus for the corresponding user and given proper access rights.

   user@host:~> mkdir -p ~/.globus
   user@host:~> mv usercert.pem ~/.globus/
   user@host:~> mv userkey.pem ~/.globus/
   user@host:~> chmod 700 ~/.globus
   user@host:~> chmod 600 ~/.globus/*

Create another directory ``~/.globus/certificates/`` and place all the `CA files <http://winnetou.surfsara.nl/deisa/certs/globuscerts.tar.gz>`_ there. Just untar them into the directory. These files are needed to later verify your certificate against the Certificate Authority.

Install the `GridFTP Client <http://toolkit.globus.org/toolkit/docs/6.0/admin/install/#install-bininst>`_.

Now you should be able to run::

  $ grid-proxy-init 

This tool verifies the validity of your certificate and creates a proxy, that is internally needed by the GridFTP client. This step has to be repeated before the usage. If something like::

  Your identity: <YourDNhere>
  Creating proxy ............................................... Done
  Your proxy is valid until: Wed Apr 18 22:25:32 2012

shows up, everything is installed correctly. 

---------------
Firewall issues
---------------

Because there is a distinction between control and data connection, some ports of the firewall on the client side have to be opened:

- Port 2812 for the control channel to the frontend node ``gridftp-fr1.hww.de`` (HERMIT) or ``gridftp-fr2.hww.de`` (LAKI)
- Ports 20000-20500 for data channels to the backend node (Hostnames on request. These ports have to be opened for both incoming and outgoing connections.

Moreover, you have to set the following environment variables to instruct your client to use the specified ports::

  $ export GLOBUS_TCP_PORT_RANGE=20000,20500
  $ export GLOBUS_TCP_SOURCE_RANGE=20000,20500

Please refer to this document for further information: http://www.globus.org/toolkit/docs/latest-stable/gridftp/user/#gridftp-user-config-client-firewall
