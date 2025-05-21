## 1. Install Docker  and clone the app
Download and install Docker the git clone the app 

## 2. Start the App  
Start the app in the background, in the app root:  `docker-compose up -d`

## 3. Restart After Code Changes  
If you make changes to the scripts, restart the container:  `docker-compose restart model`

## 4. Rebuild After Image or Requirements Changes  
If the "Dockerfile" or "requirements.txt" change, rebuild it:  `docker-compose up --build`
Or do a clean rebuild:  `docker-compose down` then `docker-compose up -d`