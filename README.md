# Edge router interface latency tester
This repo cotains scripts and instructions to create a job in edge router to ping a destination and post it's status to a monitoring app

# Getting started
- Download the python script and the config and place it in the `/config/scripts` folder
- Make sure the monitoring utility is running
- Modify the config and update the `status_url` with your monitor url for pushing status
- Set the destination in config you want to test latency against
- Run the script, check if the status is being correctly registered
- To run the script repeatedly, either create a systemctl service or a cron
- Adjust frequency of job as needed

# Systemctl setup
- Use the systemctl.service template config provided and create a service file
- Use command to enable the service `sudo systemctl enable <service-file-name>.service`, this auto starts the service during restart
- Use commadnn to start it `sudo systemctl start <service-file-name>.service`
