docker_hub='pchahal24'
repo='rich-table'
tag=$1
if [ -z $tag ]
then
  tag='latest'
fi
image_url='$docker_hub/$repo'
sudo docker pull $image_url:$tag
sudo docker ps | grep $repo | awk '{print $1}' | xargs sudo docker stop
sudo docker rm $repo
sudo docker run -d -p 5000:5000 --restart=always --name $repo $image_url:$tag

