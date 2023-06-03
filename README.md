# 前後端個人網站實作

個人網站入口
https://backendtest-388621.de.r.appspot.com/

## 開發利用到的工具跟觀念

* React framework:
    * class component, state, lifetime
    * axios 處理ajax
    * 一般class .css做刻劃 
    
* Django framework:
    * 原生django ORM 互動
    * rest framework 實現 RESTful API
    * simplejwt 可快速建立 jwt 作為認證token
    * sqlite 作為測試資料庫
 
 
* GCP:
    * app engine (前後端基本設定佈署成功)
    * cloud run/app engine使用cloud sql,secret manager (Fail)
    * 後端nignx-unicorn (fail)
    
## api功能
* 登入
* 登出
* 註冊
* 留言


過程中遇到的問題需要學習:

* docker容器預防系統環境問題
* gcp k8s容器佈署
* CICD 流程佈署自動化節省成本時間
* 等等devops延伸

* contextAPI管理state
* webpack打包

* corsheader 問題
* 保護settings重要key資料 
* 其他auth跟permission加密問題
* nginx

