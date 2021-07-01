FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y cmake coinor-libcbc-dev coinor-libclp-dev coinor-libcoinutils-dev coinor-libosi-dev coinor-libcgl-dev doxygen libbz2-dev bison flex g++ git make python3 bzip2 wget zlib1g-dev libgsl-dev texlive-base gawk curl default-jre python3-pip
RUN pip3 install setuptools

RUN curl -o /usr/local/lib/antlr-4.9.2-complete.jar https://www.antlr.org/download/antlr-4.9.2-complete.jar

RUN git clone https://github.com/karpase/pythonpddl.git /root/pythonpddl
RUN (cd /root/pythonpddl; make)
RUN (cd /root/pythonpddl; python3 /root/pythonpddl/setup.py build)
RUN (cd /root/pythonpddl; python3 /root/pythonpddl/setup.py install)

RUN git clone https://github.com/karpase/SituatedTemporalPlanningExperiment.git /root/SituatedTemporalPlanningExperiment

RUN git clone https://github.com/KCL-Planning/VAL.git /root/VAL
RUN mkdir /root/VAL/build
RUN (cd /root/VAL/build; cmake ..)
RUN (cd /root/VAL/build; make)

RUN cp /root/VAL/build/bin/Validate /root/SituatedTemporalPlanningExperiment/val
RUN cp /root/VAL/build/bin/libVAL.so /root/SituatedTemporalPlanningExperiment/

