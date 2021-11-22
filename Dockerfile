# using ubuntu base image
FROM ubuntu:20.04

# Use default  answers for all questions.
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get -y install clangd cmake build-essential python3-pip vim git && \
    pip3 install clang-format cmake-format 

COPY . /app

RUN cd app && cmake -D ENABLE_TESTING=ON -B build && cmake --build build && cd build && ctest --verbose
