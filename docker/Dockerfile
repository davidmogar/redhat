ARG TOMCAT_TAG="9.0"

FROM tomcat:${TOMCAT_TAG}

MAINTAINER contact@davidmogar.com

ARG TOMCAT_TAG

WORKDIR /usr/local/tomcat/webapps

RUN echo ${TOMCAT_TAG} && curl -L -O https://tomcat.apache.org/tomcat-${TOMCAT_TAG}-doc/appdev/sample/sample.war

EXPOSE 8080

CMD ["catalina.sh", "run"]
