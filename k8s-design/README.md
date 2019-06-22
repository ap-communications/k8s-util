# k8sの設計を考えるディレクトリ

# 収容性/スケーラビリティと性能
### 性能試験
- [locustをkubernetes上で構築して分散負荷テストしてlinkerdでサービスメッシュのデバッグを行う](#locustをkubernetes上で構築して分散負荷テストしてlinkerdでサービスメッシュのデバッグを行う)


# 耐障害性
### 耐障害性設計

### 耐障害性試験
- [postgresql-on-k8sで障害テスト1-dbノード](#postgresql-on-k8sで障害テスト1-dbノード)
- [high-reliability-infrastructure-migrations](#high-reliability-infrastructure-migrations)

### 障害対応/OnCallReadiness
- [brendan-gregg---cloud-performance-root-cause-analysis-at-netflix](#brendan-gregg---cloud-performance-root-cause-analysis-at-netflix)
- [プロダクションレディマイクロサービス](#プロダクションレディマイクロサービス)
---

## LocustをKubernetes上で構築して分散負荷テストして、Linkerdでサービスメッシュのデバッグを行う
https://www.1915keke.com/entry/2018/10/06/030425

---
## PostgreSQL on k8sで障害テスト(1) DBノード
https://qiita.com/tzkoba/items/b412ccd0fd3c7f6a4ab4

## High Reliability Infrastructure migrations 
https://speakerdeck.com/jvns/high-reliability-infrastructure-migrations?slide=12

- 手書きスライドの人
- k8sの色々なコンポーネントに疑似障害を発生させながら、性能エンジニアリングを進めていく

---
## how kubernetes can break by etcd
https://twitter.com/b0rk/status/1108154770211119104
- SPOFのetcdが死ぬとk8sは完全停止する
- slow diskでもやっぱり死ぬ

---
## Brendan Gregg - Cloud Performance Root Cause Analysis at Netflix
https://twitter.com/deeeet?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor

- 障害シナリオ毎のMethotologyの準備

## プロダクションレディマイクロサービス
https://www.oreilly.co.jp/books/9784873118154/

- production ready check listがとても参考になる

## kubernetes-failure-stories
https://github.com/hjacobs/kubernetes-failure-stories

- 各社の障害事例集
