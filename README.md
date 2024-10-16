# Teams Llama

A Llama bot in Teams allows you to chat directly with your Llama instance (or other Ollama models) and can also be added to an existing channel to interact with team members.

This bot has been build upon the work of [rvinothrajendran](https://github.com/rvinothrajendran/PythonBotTeamAppDevelopment), 01EchoBot sample.

## Prerequisites

- Docker and Docker Compose
- Domain name with SSL certificate
- Company admin Azure (Microsoft) account, with an App registration with a Secret key, Chat permissions and an Azure Bot with the teams channel enabled and the https://your_domain/api/messages messaging endpoint
- Nvidia GPU (for AMD change docker-compose file to AMD device)

## Instructions

1. Run `git clone https://github.com/victornemeth/teamsllama.git && cd teamsllama`
2. Run `nano config.py` and put in your APP ID and SECRET KEY
3. Run `docker compose up -d`
4. Run `docker exec -it ollama ollama pull llama3.1:8b`

4. Go to localhost:81 in browser or to your_local_ip:81 if you are on another machine
5. Login (Default Proxy Manager username: admin@example.com. Default Proxy Manager password: changeme)
6. Add proxy host
7. Put in Domain Name
8. Forward Hostname: teams-bot; Forward Port: 3978
9. Force SSL
10. Go to your Azure Portal, in the Azure Bot Channels, click **Open in Teams**
11. Chat with your model
