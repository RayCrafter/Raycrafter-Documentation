=======
Gridftp
=======

`GridFTP <https://wickie.hlrs.de/platforms/index.php/Data_Transfer_with_GridFTP>`_ can be used for high-performance data transfer. Alternative, more extensive guide can be found `here <https://wickie.hlrs.de/dgrid/>`_.
In order to use it, a lot of 'paperwork' has to be done.

-----------------
X.509 certificate
-----------------

You need a certifiacte to use the service. For the Univeristy of Stuttgart, contact Thomas Beisel.
He is part of the RA of the DFN (Deutsches Forschungsnetz). You have to send im a certificate request.
A good general guide can be found at the `DFN <https://www.pki.dfn.de/fileadmin/PKI/anleitungen/Anleitung_Nutzung_OpenSSL.pdf>`_.
Be aware that there are some special requirements:

  - If you have a server that uses GridFTP, see the `robot certificate FAQ <https://www.pki.dfn.de/faqpki/faqpki-grid/>`_.
  - See this `list <https://info.pca.dfn.de/grid-ras.html>`_ of RAs and for who to contact.
    Note that you should use ``/C=DE/O=GridGermany/OU=<Name of the institute>`` when creating a certificate request.

Here are the commands i used in order to  create the certificate request::

  $ openssl genrsa -des3 -out gridftp.pem 4096  
  $ openssl req -batch -sha1 -new -key gridftp.pem -out request.pem -subj '/C=DE/ST=BW/L=Stuttgart/O=GridGermany/OU=Universitaet Stuttgart/CN=Robot- RenderManager Server - David Zuber/emailAddress=zuber.david@gmx.de'f

Send the request to the contact person. The DN of the certificate you receive has to be sent to the HLRS, as stated in the wiki.
You also have to open some ports in your firewall. The hostnames of the backend-nodes will be given to you upon request only!
