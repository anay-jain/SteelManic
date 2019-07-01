#! /bin/bash

ssh -i ~/.ssh/keys/deploy.pem steelmanic@steelmanic.com "cd ~/frontends/website/ && git pull"
