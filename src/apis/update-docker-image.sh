tag=$1
if [ -z $tag ]
then
  tag='latest'
fi
sudo docker pull pchahal24/rich-table:$tag
sudo docker ps | grep rich-table | awk '{print $1}' | xargs sudo docker stop
sudo docker rm rich-table
sudo docker run -d -p 5000:5000 --restart=always --name rich-table  pchahal24/rich-table:$tag

