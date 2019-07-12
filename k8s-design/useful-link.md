# k8sの設計を考えるためのリンク集

# 目次
## 1.収容性/スケーラビリティと性能
### 1-1.性能/収容性設計
- [Kubernetesアンチパターン](#Kubernetesアンチパターン)

### 1-2.性能試験
- [locustをkubernetes上で構築して分散負荷テストしてlinkerdでサービスメッシュのデバッグを行う](#locustをkubernetes上で構築して分散負荷テストしてlinkerdでサービスメッシュのデバッグを行う)


## 2.耐障害性
### 2-1.耐障害性設計
- TBD

### 2-2.耐障害性試験
- [postgresql-on-k8sで障害テスト1-dbノード](#postgresql-on-k8sで障害テスト1-dbノード)
- [high-reliability-infrastructure-migrations](#high-reliability-infrastructure-migrations)

## 3.運用性
### 3-1.Upgradeの時の方法論
- TBD

### 3-2.障害対応/OnCallReadiness
- [brendan-gregg---cloud-performance-root-cause-analysis-at-netflix](#brendan-gregg---cloud-performance-root-cause-analysis-at-netflix)
- [プロダクションレディマイクロサービス](#プロダクションレディマイクロサービス)

### 3-3.バックアップ＆リストア
- [SpotifyがミスによりKubernetesの本番クラスタを二度も削除。しかし顧客へのサービスにほとんど影響しなかったのはなぜか？](#SpotifyがミスによりKubernetesの本番クラスタを二度も削除)
---

## Kubernetesアンチパターン
https://nekop.github.io/slides/hbstudy78.html#/

---

## LocustをKubernetes上で構築して分散負荷テストして、Linkerdでサービスメッシュのデバッグを行う
https://www.1915keke.com/entry/2018/10/06/030425

---
## PostgreSQL on k8sで障害テスト(1) DBノード
https://qiita.com/tzkoba/items/b412ccd0fd3c7f6a4ab4

## High Reliability Infrastructure migrations 
https://speakerdeck.com/jvns/high-reliability-infrastructure-migrations?slide=12

- [手書きスライドの人](https://jvns.ca/)
- k8sの色々なコンポーネントに疑似障害を発生させながら、性能エンジニアリングを進めていく

---
## how kubernetes can break by etcd
https://twitter.com/b0rk/status/1108154770211119104
- SPOFのetcdが死ぬとk8sは完全停止する
- slow diskでもやっぱり死ぬ

---
## Brendan Gregg - Cloud Performance Root Cause Analysis at Netflix
http://www.brendangregg.com/blog/2019-04-26/yow2018-cloud-performance-netflix.html

- 障害シナリオ毎のMethotologyの準備

## プロダクションレディマイクロサービス
https://www.oreilly.co.jp/books/9784873118154/

- production ready check listがとても参考になる

## kubernetes-failure-stories
https://github.com/hjacobs/kubernetes-failure-stories

- 各社の障害事例集

## 10 Ways to Shoot Yourself in the Foot with Kubernetes
https://www.youtube.com/watch?v=QKI-JRs2RIE

- k8sのトラブル集、DNSの故障、container runtimeの不具合、etc

## SpotifyがミスによりKubernetesの本番クラスタを二度も削除
https://www.publickey1.jp/blog/19/spotifykubernetes.html#

- バックアップ＆リストア試験超大事という話
