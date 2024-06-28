# Node Graph Tech Demo for IT Systems based on Jaal

## Overview

This project demonstrates a node network of IT systems and their dependencies on each other. Each node represents an IT system managed by a specific team, and the edges between nodes indicate the type and nature of interactions between these systems.

## Features

- **Node Details**: Each node displays the system title, managing team, and a unique ID.
- **Edge Details**: Each edge contains information about the interaction between systems, including:
  - Connection type (e.g., Data Flow, API Call)
  - Direction (e.g., One-way, Two-way)
  - Latency
  - Throughput
  - Protocol (e.g., HTTP, TCP/IP)
  - Status (Active/Inactive)
  - Last updated date
  - Error rate
  - Description
  - Reliability

## Demo Filters

The demo allows you to apply filters to view specific subsets of the network. Examples include:

1. **Country Filter**:
    'country=='Italy' or country=='Norway''

2. **Employees Filter**:
    'employees>8'

## Running the Demo

'http://localhost:8050'
