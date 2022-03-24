# using ubuntu base image
FROM ubuntu:20.04

# Use default  answers for all questions.
ENV DEBIAN_FRONTEND noninteractive

# Upgrade the system
RUN apt-get update && apt-get upgrade -y --allow-downgrades

# install basics
RUN apt-get -y install lsb-release wget software-properties-common

# Install compilers and all tooling
RUN apt-get -y install cmake build-essential python3-pip checkinstall vim git

# Install LLVM 13 (clang toolchain)
RUN wget https://apt.llvm.org/llvm.sh && \
    chmod +x llvm.sh && \
    ./llvm.sh 13

RUN apt-get -y install clang-format-13 clang-tidy-13

# Install cmake-format with pip
RUN pip install cmake-format distro

# Copy the files to the image
COPY cmake/ /starter/cmake
COPY core/ /starter/core
COPY app/ /starter/app
COPY CMakeLists.txt /starter/CMakeLists.txt

# copy clang config files
COPY .clang-format /starter
COPY .clang-tidy /starter
COPY .cmake-format.yaml /starter

# Copy the python devkit tooling
COPY devkit /starter/devkit
COPY tooling /starter/tooling

WORKDIR /starter

# format the project
RUN ./devkit clang --format

# Build Entire project with tests and examples on
RUN ./devkit compile --clang

# Statically analyze the project
RUN ./devkit clang --lint

# Run tests. If you did not build a project,
# make sure to comment out the tests for that project
RUN cd build/core && ctest -VV
RUN ./build/core/examples/starter_core_example_one.bin
RUN cd build/app && ctest -VV
RUN ./build/app/src/starter_app.bin
