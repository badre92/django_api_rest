FROM ubuntu:14.04


#================================================
# Installations package linux
#================================================

RUN apt-get update
RUN apt-get install -y 	vim
RUN apt-get install -y 	wget
RUN apt-get install -y 	curl
RUN apt-get install -y 	build-essential
RUN apt-get install -y 	python-setuptools

RUN easy_install pip

#==================
# Vim highlight
#==================

RUN echo "syntax on" >> /etc/vim/vimrc


#================================================
# Python - Install Anaconda
#================================================


ENV downloads /downloads
RUN mkdir $downloads

ENV anaconda_url https://repo.continuum.io/archive/Anaconda3-5.0.0.1-Linux-x86_64.sh
ENV anaconda_path /opt/anaconda
ENV PATH $anaconda_path/bin:$PATH

RUN wget -nv -O $downloads/anaconda.sh $anaconda_url
RUN /bin/bash $downloads/anaconda.sh -b -p $anaconda_path
#============================
# Install env
#============================
RUN conda create -n python35 python=3.5 anaconda
#============================
# Install packages
#============================
ADD requirements.txt .

RUN /bin/bash -c " source activate python35 				&&\
    pip install django						&&\
    pip install djangorestframework         &&\
    pip install requests					&&\
    pip install selenium					&&\
    pip install pyvirtualdisplay			&&\
    pip install unittest-xml-reporting		&&\
    while read requirement; do pip install $requirement; done < requirements.txt "
#============================
# Install requirements
#============================


#============================
# Clean up
#============================

RUN apt-get 	clean
RUN rm -rf 		/var/lib/apt/lists/*
RUN rm 			$downloads/anaconda.sh
RUN conda clean -yt

ENV PATH $anaconda_path/bin:$PATH:/home/LinkMaster
ADD . /home/apirest

CMD /opt/anaconda/envs/python35/bin/python /home/apirest/manage.py runserver