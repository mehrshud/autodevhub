# File: output.tf

output "ec2_instance_id" {
  value = aws_instance.autodevhub.id
  description = "ID of the EC2 instance"
}

output "ec2_instance_public_ip" {
  value = aws_instance.autodevhub.public_ip
  description = "Public IP of the EC2 instance"
}

output "ec2_instance_public_dns" {
  value = aws_instance.autodevhub.public_dns
  description = "Public DNS of the EC2 instance"
}

output "rds_instance_endpoint" {
  value = aws_db_instance.autodevhub.endpoint
  description = "Endpoint of the RDS instance"
}

output "s3_bucket_name" {
  value = aws_s3_bucket.autodevhub.bucket
  description = "Name of the S3 bucket"
}
