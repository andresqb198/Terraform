variable "AWS_REGION"{
  type = string
  default = "us-east-1"
}

variable "AMIS" {
  type = map(string)
  default = {
    us-east-1 = "my ami"
  }
}