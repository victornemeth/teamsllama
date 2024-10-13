# Teams Llama

Llama bot in Teams.

This bot has been build upon the work of [rvinothrajendran](https://github.com/rvinothrajendran/PythonBotTeamAppDevelopment), 01EchoBot sample.
This bot has been created using [Bot Framework](https://dev.botframework.com), it shows how to create a simple bot that accepts input from the user and echoes it back.

## Prerequisites

- Docker and Docker Compose
- Domain name
- Company admin azure (microsoft) account
- Nvidia GPU (for AMD change docker-compose file to AMD device)

## Instructions

1. Run `git clone https://github.com/victornemeth/teamsllama && cd teamsllama`
3. Run `docker compose up -d`
4. Run `docker exec -it ollama ollama pull llama3.1:8b`

4. Go to localhost:81 in browser or to your_local_ip:81
5. Login (Default Proxy Manager username: admin@example.com. Default Proxy Manager password: changeme)
6. Add proxy host
7. Put in Domain Name
8. Forward Hostname: teams-bot; Forward Port: 3978
9. Force SSL
