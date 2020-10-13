MAINTAINER 
sets the Author field of the image (useful when pushing to Docker Hub)

&& \ 
isn’t Docker specific, but tells Linux to run the next command as part of the existing line (instead of using multiple RUN directives, you can use just one)

COPY 
copies files from the first parameter (the source .) to the destination parameter (in this case, /app)

WORKDIR 
sets the working directory (all following instructions operate within this directory); you may use WORKDIR as often as you like

ENTRYPOINT 
configures the container to run as an executable; only the last ENTRYPOINT instruction executes
