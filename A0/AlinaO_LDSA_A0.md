# Task 1: Questions
1. A private IP address is assigned to the instance's network interface by the server and is part of a private network that is used for communication between instances in the same broadcast domain by a virtual switch or accessible by virtual router. A floating IP is not using any service or being statically set within the guest. The private IP will be used for accessing the instance by other instances in private networks while the floating IP address would be used for accessing the instance from public networks.

2. No you cannot access the Internet from the instance without assigning a floating IP to the machine because the floating IP is used for each new Instance to create a new connection.

3. A snapshot is a sub-type of images and are instantaneous copies of instances that contain an image of the state of the filesystem at the moment the snapshot is taken. An image is a bootable filesystem containing an operating system and are the basis of instances. An instance is the term for a virtual machine, it is functionally identical to a physical server but can be created or destroyed and things such as operating system, storage space, RAM and virtual CPU can be modified.

4.
  a.) OpenStack Image Service is called Glance 
  b.) OpenStack Compute is called Nova

5. Booting from an image(snapshot) will create an instance containing a clean Operating system while booting from a volume(snapshot) creates an instance based on a previously used instance that has been saved in storage.

6. Changes to your instance context will not be saved after deleting the instance.

7.For an instance booted by createing a new volume, changes to the instance will persist on the volume after deleteing the insance only if you select 'No' for the option "Delete Volume on Instance Delete".

8. Snapshots preserve the state and data of a virtual machine at a specific point in time, including the vm’s power state (i.e. powered-on, powered-off, suspended) and data that consists of all of the files that make up the vm(i.e disks, memory, and other devices). VM snapshots can be used as a quick failsafe roll back point before performing upgrades, changing installed software, uninstalling components, etc. A VM or set of VMs can have snapshots created for testing to develop and validate code changes.

9. Creating a New Volume upon launching an instance enables persistent storage through creating a block storage devices that you attach to instances. You would want to "Delete Volume on Instance Delete" unless you want to use the attached volume for other instances.

# Task 2: Questions
1. The name of the OpenStack service providing volumes is the Block storage service Cinder.

2. Cinder only allows a volume to be attached to a single host or instance.

3. Ephemeral storage is the volatile temporary storage attached to your instances which is only present during the running lifetime of the instance. In the case that the instance is stopped or terminated or underlying hardware faces an issue, any data stored on ephemeral storage would be lost. Yes, each instance by default has ephemeral storage.

4. Block storage is implemented in OpenStack by the Block Storage service (cinder). Because these volumes are persistent, they can be detached from one instance and re-attached to another instance and the data remains intact. The main difference is that ephemeral is temporary while Block Storage is persistent. Ephemeral storage has the main application of running the operating system and scratch space. Block Storage adds additional persistent storage to a virtual machine (VM).Object Storage has the main application of storing data, including VM images. Shared filed system storage adds additional persistent storage to a virtual machine.

# Task 3: Questions 
1. The "Network Topology" image is a graphical representation of the connection of the openstack server to the many instances and the external public network. 

2.

3. A provider network will be used as the external gateway network and a tenant network will be used for instances. A router will be used to route traffic from the tenant network to the Internet, and floating IPs will be used to provide direct connectivity to instances.

4. A router is a networking device that forwards data packets between computer networks. Routers perform the traffic directing functions on the Internet. 

5. 

6. The project code name for Networking Services is neutron.
# Task 4: Questions

1. A pseudo file system maintains information about the currently running system that doesn't persist across reboots, it exists while the system in running only in RAM. In UNIX filesystems folders indicate devices as they are connected and they are created dynamically based on hardware hierarchy. 

2.  Though Amazon's "S3 bucket" and OpenStack's object store are different APIs, they have the same architectural concepts and building blocks where data is stored in blobs called Objects that can be uploaded and downloaded via the API.

3. The name of the OpenStack service providing the Object Store is Swift


# References

* Task 1.9 https://docs.openstack.org/horizon/latest/user/manage-volumes.html
* Task 1.7/1.9 https://ubccr.freshdesk.com/support/solutions/articles/13000046549-launching-openstack-instances
* Task 2.4 https://docs.openstack.org/arch-design/design-storage/design-storage-concepts.html
* Task 3.3 https://subscription.packtpub.com/book/virtualization_and_cloud/9781783983308/6/ch06lvl1sec34/demonstrating-traffic-flow-from-instance-to-internet
