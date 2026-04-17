#Creat New Project
'''sh
mvn archetype:generate \
-DgroupId=com.mycompany.app \
-DartifactId=my-app \
-DarchetypeArtifactId=maven-archetype-quickstart \
-DarchetypeVersion=1.4 \
-DinteractiveMode=false
'''
'''
mvn -B archetype:generate \
 -DarchetypeGroupId=software.amazon.awssdk \
 -DarchetypeArtifactId=archetype-lambda -Dservice=s3 -Dregion=ap-southeast-1 \
 -DarchetypeVersion=2.21.29 \
 -DgroupId=com.example.myapp \
 -DartifactId=myapp
 
 '''