==========
Scheduling
==========

This section explains how to manually submit a job on a cluster

---------------------
HLRS Hornet/Hazel Hen
---------------------

++++
qsub
++++

``qsub`` is a little tool for submitting jobs to the queue on the hornet.
By running the tool you inform the queue that you want to start a job and need a certain amount of recources for that. Usually you submit a batchscript. After waiting in the queue the scipt  gets executed by the MOM nodes. Here you run ``aprun`` commands to start a process on the compute nodes with the desired ressources.

+++++
aprun
+++++

``aprun`` is another tool for sending a process to the compute nodes. Once an executable or batch script gets submitted with ``aprun`` all subprocesses also run on the compute nodes.
One aprun command needs at least one free node reserved by ``qsub``.

``aprun`` has a lot of options for optimizing. The defaults might have a great negative impact on the performance of the render process. The tweaking of ``aprun`` can be quite difficult and requires expert knowledge and probably a lot of testing.

For more information on scheduling, especially how to run Arnold contact Stefan Andersson. He is Technical Sales and Appliaction Support for Cray Computer Deutschland GmbH at the HLRS.

Stefan Andersson:

  :tel: +49 711 656 91506
  :email: stefan@cray.com
  :homepage: cray.com
