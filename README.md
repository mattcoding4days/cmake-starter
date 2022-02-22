<div align="center">
  <img width="400" height="300" src="repo_assets/Cmake-Starter.png">
</div>

<br>
<div align="center">
  <img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/mattcoding4days/cmake-starter/Unittests?label=Build%2FUnittests&logo=github&style=flat-square">
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/mattcoding4days/cmake-starter?color=red&label=Issues&logo=github&style=flat-square">
  <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/mattcoding4days/cmake-starter?color=blue&label=Pull%20Requests&logo=github&style=flat-square">
  <img alt="GitHub forks" src="https://img.shields.io/github/forks/mattcoding4days/cmake-starter?label=Forks&logo=github&style=flat-square">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/mattcoding4days/cmake-starter?label=Stars&logo=github&style=flat-square">
  <img alt="GitHub" src="https://img.shields.io/github/license/mattcoding4days/cmake-starter?color=blue&label=License&logo=github&style=flat-square">
  <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/mattcoding4days/cmake-starter?color=blue&logo=github&style=flat-square">
  <img alt="Lines of code" src="https://img.shields.io/tokei/lines/github/mattcoding4days/cmake-starter?label=Total%20Lines%20Of%20Code&logo=github&style=flat-square">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/mattcoding4days/cmake-starter?label=Repo%20Size&logo=github&style=flat-square">
</div>

## :information_source: About 

> A lightweight Cmake project that uses CPM as its package manager

## :package: Docker

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

## :package:
