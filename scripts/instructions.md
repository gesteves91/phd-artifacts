# Instructions

To identify such smells we relied on the Organic tool. If you want to run the Organic tool to asses the smell collection process, you can, for instance, for the project `ant`, execute the following command:

```bash
java -jar organic-OPT.jar -sf ../projects/ant/organic/ant.json -src "../bad-smells-defects/projects/ant"
```

You can execute the `organic-OPT.jar` included inside the [scripts](scripts/) folder. We highlight that Organic needs to be run on OpenJDK 11, so you need to change the java version in case it is not the required one.