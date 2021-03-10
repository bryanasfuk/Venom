# Using Groovy
FROM biansepang/weebproject:groovy

# Clone repo and prepare working directory
RUN git clone -b master https://github.com/bryanasfuk/Venom /home/Venom/
RUN mkdir /home/Venom/bin/
WORKDIR /home/Venom/

# Make open port TCP
EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
