# Household Inventory Tracker

A simple, self-hosted web application for tracking household essentials like toilet paper, toothpaste, and more. Built with Flask, SQLite, and Docker for easy deployment.

![App Screenshot](https://via.placeholder.com/800x400?text=Household+Inventory+App) <!-- Replace with actual screenshot -->

## Features
- Add, edit (name/quantity), and delete items
- Increment/decrement quantities or set exact values
- Persistent data storage (SQLite database)
- Responsive web UI
- One-command Docker deployment
- Works on Windows, Linux, macOS, Raspberry Pi, or any VPS

## Quick Start

### Prerequisites
- [Docker](https://www.docker.com/products/docker-desktop/) installed
- [Docker Compose](https://docs.docker.com/compose/install/) (included with Docker Desktop)

### Deploy with Git Clone (Recommended)
```bash
git clone https://github.com/mythtechs/household-inventory.git
cd household-inventory
docker compose up -d --build
