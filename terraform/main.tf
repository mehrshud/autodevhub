# terraform/main.tf

# Provider Configuration
provider "aws" {
  region = var.region
}

# Variables
variable "region" {
  type        = string
  default     = "us-east-1"
  description = "AWS Region"
}

variable "instance_type" {
  type        = string
  default     = "t2.micro"
  description = "Instance Type"
}

variable "key_name" {
  type        = string
  description = "Key Pair Name"
}

# VPC and Subnet
resource "aws_vpc" "autodevhub_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "AutoDevHub-VPC"
  }
}

resource "aws_subnet" "autodevhub_subnet" {
  vpc_id            = aws_vpc.autodevhub_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "${var.region}a"
  tags = {
    Name = "AutoDevHub-Subnet"
  }
}

# Security Group
resource "aws_security_group" "autodevhub_sg" {
  name        = "autodevhub_sg"
  description = "Security Group for AutoDevHub"
  vpc_id      = aws_vpc.autodevhub_vpc.id

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
}

# EC2 Instance for Python and TypeScript
resource "aws_instance" "autodevhub_ec2" {
  ami           = "ami-0c94855ba95c71c99"
  instance_type = var.instance_type
  vpc_security_group_ids = [aws_security_group.autodevhub_sg.id]
  subnet_id = aws_subnet.autodevhub_subnet.id
  key_name               = var.key_name

  tags = {
    Name = "AutoDevHub-EC2"
  }
}

# S3 Bucket for Terraform State
resource "aws_s3_bucket" "autodevhub_s3" {
  bucket = "autodevhub-s3-bucket"
  acl    = "private"

  versioning {
    enabled = true
  }

  tags = {
    Name = "AutoDevHub-S3"
  }
}

# Outputs
output "instance_id" {
  value       = aws_instance.autodevhub_ec2.id
  description = "ID of the EC2 instance"
}

output "instance_public_ip" {
  value       = aws_instance.autodevhub_ec2.public_ip
  description = "Public IP of the EC2 instance"
}

output "s3_bucket_name" {
  value       = aws_s3_bucket.autodevhub_s3.id
  description = "Name of the S3 bucket"
}
