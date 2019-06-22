# k8sの設計を考えるディレクトリ

## 性能試験
- [locustをkubernetes上で構築して分散負荷テストしてlinkerdでサービスメッシュのデバッグを行う](#locustをkubernetes上で構築して分散負荷テストしてlinkerdでサービスメッシュのデバッグを行う)


## 耐障害性試験
- [postgresql-on-k8sで障害テスト1-dbノード](#postgresql-on-k8sで障害テスト1-dbノード)
---

## LocustをKubernetes上で構築して分散負荷テストして、Linkerdでサービスメッシュのデバッグを行う
https://www.1915keke.com/entry/2018/10/06/030425

---
## PostgreSQL on k8sで障害テスト(1) DBノード
https://qiita.com/tzkoba/items/b412ccd0fd3c7f6a4ab4

## how kubernetes can break by etcd
https://twitter.com/b0rk/status/1108154770211119104
- SPOFのetcdが死ぬとk8sは完全停止する
- slow diskでもやっぱり死ぬ
