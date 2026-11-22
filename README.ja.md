# Netheretヘルプデスク ステップ12：レポート

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

授業のための作例です。16のステップで、小さな会社のITを支える架空の会社Netheretのために、ヘルプデスクのWebアプリを作っていきます。 このステップでは、マネージャーにレポートのページを用意します。SQLクエリで計算したKPIと、素のJavaScriptで描いた棒グラフです。

## このステップで加わるもの

- `helpdesk/reports.py`：KPIごとに小さな関数が1つずつあります。
  - 優先度別の対応中の依頼
  - 優先度別の、解決までの平均時間
  - スタッフ一人ひとりの依頼の数（合計と、まだ対応中のもの）
  - 一次解決率：完了した依頼のうち、Tier 1がエスカレーションせずに
    解決したものの割合
  - 2営業日より古い対応中の依頼
  - 今週完了した訪問作業と、過去の作業のうち完了になっているものの割合
  - 最も役に立ったナレッジベースの記事
- `helpdesk/templates/reports.html`：主な数字と、KPIごとの
  表。
- `helpdesk/static/js/charts.js`：各 `table.chart` を見つけ、その上の `<canvas>` に
  表の数字を読んで棒グラフを描きます。

## 動かしてみる

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

`manager@netheret.example`（デモ用パスワード `password123`）でサインインし、
Reportsを開きます。依頼を解決するか作業を完了にしてから再読み込みすると、数字が
変わります。何も保存せず、ページを開いたときにすべて数えているからです。

## 注目するところ

- `func.count`、`func.avg`、`group_by`：Pythonで全行をループするのではなく、
  データベースが数えます。
- `julianday()` はSQLite独自の関数です。ほかのデータベースでは、
  日付の引き算に別の方法が必要です。
- グラフは表から描くので、両者が食い違うことはありません。
  canvasには `aria-hidden="true"` を付けています。スクリーンリーダーには
  表がすでにすべてを伝えているからです。
- `devicePixelRatio`：canvasを画面の本当の解像度で描くので、
  文字がぼやけません。

## このステップを学ぶ

これは **Task 2. Developing the solution** の16ステップ中のステップ12です。T Level Digital Software Developmentの無料レッスン（英語）のシリーズで、PythonとFlaskを使い、アジャイルのスプリントでNetheretのヘルプデスクを作ります。このステップのレッスンはこちらです：
[KPIのレポートとグラフ](https://mitsurutech.co.uk/resources/t-level/dsd-t2-12-reports)。

- 前のステップ：[ステップ11「顧客から見た依頼」](https://github.com/mitsurutech/netheret-helpdesk-11-customer-view)
- 次のステップ：[ステップ13「アクセシビリティの設定」](https://github.com/mitsurutech/netheret-helpdesk-13-accessibility)
- [T Level Digitalの無料レッスン一覧](https://mitsurutech.co.uk/resources/t-level)
- [これらのレッスンをMitsuruTechでクラスに教える](https://mitsurutech.co.uk/ja/learning)、[料金を見る](https://mitsurutech.co.uk/ja/pricing)、
  [学校で無料の1年を始める](https://mitsurutech.co.uk/ja/signup)

## この作例について

T Level Digital Software Developmentの授業のための作例として、[Mitsuru Technologies](https://mitsurutech.co.uk/ja)（MitsuruTech）が書きました。
Netheret IT Support Solutionsの課題文はPearsonのサンプル評価資料によるものです。このコードと解説は私たち自身のもので、
PearsonやDepartment for Educationが公開、推奨、承認したものではありません。
「T Level」はDepartment for Educationの登録商標です。
