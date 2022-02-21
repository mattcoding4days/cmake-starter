<div align="center">
  <h1>Cmake Starter</h1>
  <img alt="GitHub Workflow Status (event)" src="https://img.shields.io/github/workflow/status/mattcoding4days/cmake-starter/CMake?label=Unittests%2FBuild&logo=github&style=flat-square">
  <img alt="GitHub issues" src="https://img.shields.io/github/issues-raw/mattcoding4days/cmake-starter?style=flat-square">
  <img alt="GitHub" src="https://img.shields.io/github/license/mattcoding4days/cmake-starter?style=flat-square">
  <img alt="GitHub search hit counter" src="https://img.shields.io/github/search/mattcoding4days/cmake-starter/cmake?style=flat-square">
  <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/mattcoding4days/cmake-starter?style=flat-square">
  <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/mattcoding4days/cmake-starter?color=green&logo=github&logoColor=green&style=flat-square">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/mattcoding4days/cmake-starter?color=pink&logo=github&logoColor=pink&style=flat-square">
</div>

## About 

> A lightweight Cmake project that contains a shared library found in the `core` directory
> and a binary application meant to consume the shared library found in the `app` directory

## Docker

> This container builds the development environment for Ubuntu 20.04,
> installs the cmake project, and then runs the tests

### :keyboard: Commands

```bash
# Build the container (can be used to rebuild image after code changes)
# [e.g] docker image build -t <image-name>:<tag> .
docker image build -t cm:v0.1 .

# Rebuild with no cache
docker image build --no-cache -t cm:v0.1 .

# Run the container interactively
# [e.g] docker container run -it <image-name>:<tag>
docker container run -it cm:v0.1

# Run non interactively
docker container run cm:v0.1
```
