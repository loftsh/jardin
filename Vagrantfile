# -*- mode: ruby -*-

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "jardin"

  config.vm.network "forwarded_port", guest: 8080, host: 8081
  config.vm.synced_folder ".", "/code", :mount_options => ["dmode=777","fmode=700"]

  config.vm.provision "shell", path: ".install/setup.sh"
end
