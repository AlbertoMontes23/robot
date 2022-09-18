FROM ros:melodic-ros-core
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install curl -y
RUN curl -sSL http://get.gazebosim.org | sh
RUN apt-get install build-essential -y   # gcc
RUN apt-get install manpages-dev -y      #gcc
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get -y install git

CMD ["bash"]
