# terraform/variables.tf

# Variables
variable "aws_region" {
  type        = string
  default     = "us-west-2"
  description = "AWS region"
}

variable "instance_type" {
  type        = string
  default     = "t2.micro"
  description = "AWS instance type"
}

variable "ami_id" {
  type        = string
  default     = "ami-0c94855ba95c71c99"
  description = "AWS AMI ID"
}

variable "vpc_cidr" {
  type        = string
  default     = "10.0.0.0/16"
  description = "VPC CIDR block"
}

variable "subnet_cidr" {
  type        = string
  default     = "10.0.1.0/24"
  description = "Subnet CIDR block"
}

variable "ssh_key_name" {
  type        = string
  default     = "auto-dev-hub-ssh-key"
  description = "SSH key name"
}

# Provider configuration
provider "aws" {
  region = var.aws_region
}

# Output values
output "instance_public_ip" {
  value       = aws_instance.autodevhub.public_ip
  description = "Public IP address of the AutoDevHub instance"
}

output "instance_public_dns" {
  value       = aws_instance.autodevhub.public_dns
  description = "Public DNS name of the AutoDevHub instance"
}

# Resource definitions
resource "aws_vpc" "autodevhub" {
  cidr_block = var.vpc_cidr
  tags = {
    Name = "AutoDevHub-VPC"
  }
}

resource "aws_subnet" "autodevhub" {
  vpc_id            = aws_vpc.autodevhub.id
  cidr_block        = var.subnet_cidr
  availability_zone = "${var.aws_region}a"
  tags = {
    Name = "AutoDevHub-Subnet"
  }
}

resource "aws_internet_gateway" "autodevhub" {
  vpc_id = aws_vpc.autodevhub.id
  tags = {
    Name = "AutoDevHub-IGW"
  }
}

resource "aws_route_table" "autodevhub" {
  vpc_id = aws_vpc.autodevhub.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.autodevhub.id
  }
  tags = {
    Name = "AutoDevHub-RT"
  }
}

resource "aws_route_table_association" "autodevhub" {
  subnet_id      = aws_subnet.autodevhub.id
  route_table_id = aws_route_table.autodevhub.id
}

resource "aws_security_group" "autodevhub" {
  vpc_id = aws_vpc.autodevhub.id
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "AutoDevHub-SG"
  }
}

resource "aws_key_pair" "autodevhub" {
  key_name   = var.ssh_key_name
  public_key = file("~/.ssh/id_rsa.pub")
}

resource "aws_instance" "autodevhub" {
  ami           = var.ami_id
  instance_type = var.instance_type
  vpc_security_group_ids = [aws_security_group.autodevhub.id]
  subnet_id = aws_subnet.autodevhub.id
  key_name               = var.ssh_key_name
  user_data = file("terraform/user_data.sh")
  tags = {
    Name = "AutoDevHub-Instance"
  }
}
