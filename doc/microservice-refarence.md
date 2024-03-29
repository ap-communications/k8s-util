# Microserviceリンク集

## MicroServiceArchitecture
* [『Microservice Patterns』 まとめ](#microservice-patterns-まとめ)

## 実際の移行事例
- [クックパッド基幹システムのmicroservices化戦略](#クックパッド基幹システムのmicroservices化戦略-お台場プロジェクト1年半の軌跡)
- [マイクロサービス化を支える継続的切り替え術](#マイクロサービス化を支える継続的切り替え術)

## Tool
- [locust-コトハジメ](#locust-コトハジメ)

---
## 『Microservice Patterns』 まとめ
https://qiita.com/yasuabe2613/items/3bff44e662c922083264

- MicroServiceのパターン集を解説した記事

## 12 Factor App - モダンなサービス運営に必要な12のインフラ的要素
https://qiita.com/awakia/items/04135ea89be787be1cfc

- 10.開発環境と本番環境の一致
    - 理想
        - 時間：数分から数時間で書いたコードが本番にデプロイされる
        - 人：開発する人とデプロイする人が同じ
        - ツール：ローカルとサーバーでほぼ同じ
    - dokcerの普及により、↑のハードルがずっと下がった印象
---
## クックパッド基幹システムのmicroservices化戦略 〜お台場プロジェクト1年半の軌跡〜
https://techlife.cookpad.com/entry/2018-odaiba-strategy

- microservicesへ分割していくうえで困ることの1つが「大きな静的データの共有」の問題
    - GDBMファイルを各アプリケーションに配布

## マイクロサービス化を支える継続的切り替え術
https://techlife.cookpad.com/entry/2019/03/05/115000

- サービス分離作業とは
    - 巨大な一つのコードベースから、他に対する依存が少ない、もしくは関係のない機能・サービスなどをマイクロサービスとして分離すること
- NGINXを使ったサービス分離手法解説
---
## Locust コトハジメ
https://qiita.com/yamionp/items/17ffcc465272ad83c490)

- python製の負荷試験ツール
- 特徴
    - シナリオを Python で記述
    - 分散&スケーラブル
    - Web ベース管理画面
    - 高いカスタマイズ性

