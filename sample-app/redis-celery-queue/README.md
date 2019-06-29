# redisとceleryを使ったjob queue
## 出展
http://ariarijp.hatenablog.com/entry/2018/05/28/210849

## redisの用意
`docker run --name redis -d -p 6379:6379 redis redis-server --appendonly yes`

## workerの起動
`celery --app=tasks worker --loglevel=info -c 2`

## 

