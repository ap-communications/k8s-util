# k8sの運用手順あれこれ

## nodeの状態の確認
### 各種Pressureの発生有無

```bash
root@liva01:~# k describe node <nodename> | grep Conditions -A 6 | awk '{printf "%20-s %10-s\n", $1,$2}'
Conditions:                    
Type                 Status    
----                 ------    
MemoryPressure       False     
DiskPressure         True      
PIDPressure          False     
Ready                True  
```

### eventの閲覧

以下で時系列順にソートできる。
```bash
root@liva02:kubernetes# kubectl get events --sort-by=.metadata.creationTimestamp
LAST SEEN   TYPE      REASON                    OBJECT                        MESSAGE
39m         Normal    SuccessfulCreate          replicaset/nginx-7bb7cd8db5   Created pod: nginx-7bb7cd8db5-hbn9m
39m         Normal    SuccessfulCreate          replicaset/nginx-7bb7cd8db5   Created pod: nginx-7bb7cd8db5-czjsh
39m         Normal    ScalingReplicaSet         deployment/nginx              Scaled up replica set nginx-7bb7cd8db5 to 5
```

## クラスタ状態の確認


### kube-controller-managerのleader nodeの確認
- `holderIdentity` fieldにleader nodeのhost名が表示される

```bash
# kubectl describe endpoints kube-controller-manager -n kube-system | grep holderIdentity
                {"holderIdentity":"liva01_557e8cf3-e916-4ff9-8297-b61c8ff58b73","leaseDurationSeconds":15,"acquireTime":"2019-08-06T13:42:41Z","renewTime"...
```

### kube-schedulerのleader nodeの確認
- `holderIdentity` fieldにleader nodeのhost名が表示される

```bash
# kubectl describe endpoints kube-scheduler -n kube-system | grep holderIdentity
                {"holderIdentity":"liva01_0c868a9c-b49c-4016-99e0-842cad9fca25","leaseDurationSeconds":15,"acquireTime":"2019-08-06T13:42:25Z","renewTime"...
```

### etcdのleader nodeの確認
- V3の場合、RAFT関係の情報も取得できる
- `RAFT TERM` の意味合いについては、[Qiita:etcd総選挙を眺めてみる](https://qiita.com/ksato9700/items/9b44a95ce27ac23a94e1) を参照

```bash
root@liva01:bin# ETCDCTL_API=3 etcdctl --endpoints https://192.168.0.120:2379,https://192.168.0.121:2379,https://192.168.0.122:2379 -w table endpoint status
+----------------------------+------------------+-----------+---------+-----------+-----------+------------+--------------------+--------+
|          ENDPOINT          |        ID        |  VERSION  | DB SIZE | IS LEADER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
+----------------------------+------------------+-----------+---------+-----------+-----------+------------+--------------------+--------+
| https://192.168.0.120:2379 | 8dcfe04331fa3be7 | 3.3.0+git |  1.9 MB |     false |        79 |    4414388 |            4414388 |        |
| https://192.168.0.121:2379 | 7d14235276a52eb8 | 3.3.0+git |  1.9 MB |     false |        79 |    4414388 |            4414388 |        |
| https://192.168.0.122:2379 | cd7aeeba2adc4219 | 3.3.0+git |  1.9 MB |      true |        79 |    4414388 |            4414388 |        |
+----------------------------+------------------+-----------+---------+-----------+-----------+------------+--------------------+--------+
root@liva01:bin#
```

```bash
# ETCDCTL_API=2 etcdctl --endpoints https://<IPaddr>:<port> member list
7d14235276a52eb8: name=liva02 peerURLs=http://192.168.0.121:2380 clientURLs=https://192.168.0.121:2379 isLeader=true
8dcfe04331fa3be7: name=liva01 peerURLs=http://192.168.0.120:2380 clientURLs=https://192.168.0.120:2379 isLeader=false
cd7aeeba2adc4219: name=liva03 peerURLs=http://192.168.0.122:2380 clientURLs=https://192.168.0.122:2379 isLeader=false
```

## その他
### kubernetesがetcdに格納のデータの確認

```bash
root@liva01:bin# etcdctl --endpoints https://<IPaddr>:<port> get "" --prefix --keys-only | head
/registry/apiextensions.k8s.io/customresourcedefinitions/alertmanagers.monitoring.coreos.com
/registry/apiextensions.k8s.io/customresourcedefinitions/prometheuses.monitoring.coreos.com
/registry/apiextensions.k8s.io/customresourcedefinitions/prometheusrules.monitoring.coreos.com
/registry/apiextensions.k8s.io/customresourcedefinitions/servicemonitors.monitoring.coreos.com
/registry/apiregistration.k8s.io/apiservices/v1.
```

### etcdで特定のkey=APIオブジェクトが持つ値の確認
- `--keys-only` をつけなければ、key:valueのvalue側も確認できる
- `-w json` でjson形式で出力できるので、 `jq` でパースする
- 各URIの意味については、[こちらの記事](https://jakubbujny.com/2018/09/02/what-stores-kubernetes-in-etcd/)を参照

```bash
root@liva01:bin# ETCDCTL_API=3 etcdctl --endpoints https://<IPaddr>:<port> get "/registry/apiextensions.k8s.io/customresourcedefinitions/alertmanagers.monitoring.co
reos.com" --prefix -w json | jq .
{
  "header": {
    "cluster_id": 3851517076390931500,
    "member_id": 10218632658732857000,
    "revision": 1621438,
    "raft_term": 79
  },
  "kvs": [
    {
      "key": "L3JlZ2lzdHJ5L2FwaWV4dGVuc2lvbnMuazhzLmlvL2N1c3RvbXJlc291cmNlZGVmaW5pdGlvbnMvYWxlcnRtYW5hZ2Vycy5tb25pdG9yaW5nLmNvcmVvcy5jb20=",
      "create_revision": 131147,
      "mod_revision": 131150,
      "version": 3,
      "value": "eyJraW5kIjoiQ3VzdG9tUmVzb3VyY2VEZWZpbml0aW9uIiwiYXBpVmVyc2lvbiI6ImFwaWV4dGVuc2lvbnMuazhzLmlvL3YxYmV0YTEiLCJtZXRhZGF0YSI6eyJuYW1lIjoiYWxlcnRtYW5hZ2Vycy5tb25pdG9yaW5nLmNvcmVvcy5jb20iLCJ1aWQiOiJkNWVmNGNlNS1mMjRlLTQ0NjEtOGVkOC01ZTA2NjEyMWEzOGMiLCJnZW5lcmF0aW9uIjoxLCJjcmVhdGlvblRpbWVzdGFtcCI6IjIwMTktMDctMzFUMTY6NTM6MDBaIn0sInNwZWMiOnsiZ3JvdXAiOiJtb25pdG9yaW5nLmNvcmVvcy5jb20iLCJ2ZXJzaW9uIjoidjEiLCJuYW1lcyI6eyJwbHVyYWwiOiJhbGVydG1hbmFnZXJzIiwic2luZ3VsYXIiOiJhbGVydG1hbmFnZXIiLCJraW5kIjoiQWxlcnRtYW5hZ2VyIiwibGlzdEtpbmQiOiJBbGVydG1hbmFnZXJMaXN0In0sInNjb3BlIjoiTmFtZXNwYWNlZCIsInZlcnNpb25zIjpbeyJuYW1lIjoidjEiLCJzZXJ2ZWQiOnRydWUsInN0b3JhZ2UiOnRydWV9XSwiY29udmVyc2lvbiI6eyJzdHJhdGVneSI6Ik5vbmUifSwicHJlc2VydmVVbmtub3duRmllbGRzIjp0cnVlfSwic3RhdHVzIjp7ImNvbmRpdGlvbnMiOlt7InR5cGUiOiJOYW1lc0FjY2VwdGVkIiwic3RhdHVzIjoiVHJ1ZSIsImxhc3RUcmFuc2l0aW9uVGltZSI6IjIwMTktMDctMzFUMTY6NTM6MDBaIiwicmVhc29uIjoiTm9Db25mbGljdHMiLCJtZXNzYWdlIjoibm8gY29uZmxpY3RzIGZvdW5kIn0seyJ0eXBlIjoiRXN0YWJsaXNoZWQiLCJzdGF0dXMiOiJUcnVlIiwibGFzdFRyYW5zaXRpb25UaW1lIjpudWxsLCJyZWFzb24iOiJJbml0aWFsTmFtZXNBY2NlcHRlZCIsIm1lc3NhZ2UiOiJ0aGUgaW5pdGlhbCBuYW1lcyBoYXZlIGJlZW4gYWNjZXB0ZWQifV0sImFjY2VwdGVkTmFtZXMiOnsicGx1cmFsIjoiYWxlcnRtYW5hZ2VycyIsInNpbmd1bGFyIjoiYWxlcnRtYW5hZ2VyIiwia2luZCI6IkFsZXJ0bWFuYWdlciIsImxpc3RLaW5kIjoiQWxlcnRtYW5hZ2VyTGlzdCJ9LCJzdG9yZWRWZXJzaW9ucyI6WyJ2MSJdfX0K"
    }
  ],
  "count": 1
}
```

### CRDを含めたすべてのAPIオブジェクトの確認

```bash
# kubectl api-resources
NAME                              SHORTNAMES   APIGROUP                       NAMESPACED   KIND
bindings                                                                      true         Binding
componentstatuses                 cs                                          false        ComponentStatus
configmaps                        cm                                          true         ConfigMap
endpoints                         ep                                          true         Endpoints
events                            ev                                          true         Event
limitranges                       limits                                      true         LimitRange
```

### kubectlが見に行っているAPI endpoitとhttp response statusの確認

```bash
# k get nodes -v=6
I0808 01:28:48.167054   22396 loader.go:359] Config loaded from file:  /root/.kube/config
I0808 01:28:48.259027   22396 round_trippers.go:438] GET https://192.168.0.120:6443/api/v1/nodes?limit=500 200 OK in 75 milliseconds
I0808 01:28:48.260209   22396 get.go:564] no kind "Table" is registered for version "meta.k8s.io/v1beta1" in scheme "k8s.io/kubernetes/pkg/api/legacyscheme/scheme.go:30"
NAME     STATUS   ROLES    AGE   VERSION
liva01   Ready    <none>   8d    v1.15.1
liva02   Ready    <none>   8d    v1.15.1
```

### Evicted状態のpodの手動削除

```bash
kubectl get pods --all-namespaces -ojson | jq -r '.items[] | select(.status.reason!=null) | select(.status.reason | contains("Evicted")) | .metadata.name + " " + .metadata.namespace' | xargs -n2 -l bash -c 'kubectl delete pods $0'
```

https://github.com/kubernetes/kubernetes/issues/55051
