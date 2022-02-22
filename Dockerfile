# using ubuntu base image
FROM ubuntu:20.04

# Use default  answers for all questions.
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get -y install clangd cmake build-essential python3-pip vim git

# Copy the files to the image
COPY cmake/ /starter/cmake
COPY core/ /starter/core
COPY app/ /starter/app
COPY CMakeLists.txt /starter/CMakeLists.txt

# Build Entire project ( No tests, No Examples)
RUN cd starter && cmake -B build \
                       -D STARTER_BUILD_CORE=ON \
                       -D STARTER_BUILD_CORE_TESTING=ON \
                       -D STARTER_BUILD_CORE_EXAMPLES=ON \
                       # \
                       -D STARTER_BUILD_APP=ON \
                       -D STARTER_BUILD_APP_TESTING=ON \
                       # \
                       # \ -C to specify path for make. \
                       # \ -j to specify number of jobs (processors) to run simultaneously. \
                       # \ nproc is the number of processors on the system. \
                       && make -C build -j$(nproc)


# Run tests. If you did not build a project,
# make sure to comment out the tests for that project
RUN cd starter/build/core && ctest -VV
RUN ./starter/build/core/examples/starter_core_example_one
RUN cd starter/build/app && ctest -VV
RUN ./starter/build/app/src/starter_app.bin
