# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "geerlingguy/centos7"

  # Set up virtualbox with a private network address
  config.vm.network :private_network, ip: "192.168.56.121"
  config.ssh.forward_agent = true

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network "forwarded_port", guest: 8080, host: 8080


  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder "./app", "/var/www/schema_crc_nd_edu"

  # Prefer Virtualbox as a provider.
  config.vm.provider "virtualbox"
  # Openstack uses shell configuration downloaded
  # from OpenStack auth/security tab.
  # Prevents sensitive info from ending up in Vagrantfile
  # See: https://github.com/ggiamarchi/vagrant-openstack-provider/issues/70
  config.vm.provider "openstack" do |os, override|
        override.vm.box = "dummy"
        override.ssh.username = "centos"
        override.ssh.private_key_path = "~/.ssh/schema_crc_nd_edu"
        # Specify OpenStack authentication information
        os.openstack_auth_url = ENV['OS_AUTH_URL']
        os.username = ENV['OS_USERNAME']
        os.password = ENV['OS_PASSWORD']
        os.tenant_name = ENV['OS_TENANT_NAME']
		os.region = ENV['OS_REGION_NAME']

       # Specify instance information
		os.server_name = "schema_crc_nd_edu-test"
 		os.flavor = "RAM-2GB Disk-8GB CPU-2"
		os.image = "CRC-CentOS-6.6-x86_64"
		os.networks = "Campus - Private 1"
		os.keypair_name = "schema_crc_nd_edu"
		os.security_groups = ["default","DASPOS"] 
  end

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Run Ansible from the Vagrant Host
  # Ansible is configured to run multiple inventories
  # http://erikaheidi.com/blog/configuring-a-multistage-environment-with-ansible-and-vagrant
  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "vvv"
    ansible.playbook = "provision/provision.yml"
    ansible.inventory_path = "provision/inventories/dev"
    ansible.limit = 'all'
    ansible.extra_vars = { ansible_connection: 'ssh', ansible_ssh_args: '-o ForwardAgent=yes' }
  end

end
