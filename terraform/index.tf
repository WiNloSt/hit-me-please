provider "google" {
  credentials = "${file("credential.json")}"
  project     = "kelvin-hit-me-please"
  region      = "asia-southeast1"
  zone        = "asia-southeast1-b"
}

resource "google_compute_instance" "terraform_instance" {
  name         = "terraform-instance-${count.index}"
  machine_type = "n1-standard-2"
  count        = 3

  boot_disk {
    initialize_params {
      image = "ubuntu-1804-bionic-v20190530"
      size  = 30
    }
  }

  metadata = {
    sshKeys = "circleci:${file("~/.ssh/hitme_rsa.pub")}"
  }

  network_interface {
    network = "default"
    access_config {}
  }

  tags = ["hit-me-please"]
}

resource "google_compute_firewall" "default" {
  name    = "allow-http"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["80"]
  }

  target_tags = ["hit-me-please"]
}


output "ip" {
  value = "${google_compute_instance.terraform_instance.*.network_interface.0.access_config.0.nat_ip}"
}
