# 要旨
[arXiv](https://arxiv.org/)から自動でslackに興味のある論文を取得するbot  

# 仕組み 
arXiv API から python を用いて, 必要な分野の論文情報のパースを取得し, それをもとにIncoming Webhooksを用いてslackに流すようにした.自動実行に関しては現在はcronを用いて自動的に実行している. この部分については変更の余地あり.

![エビフライトライアングル](https://github.com/KentaSakamoto/arXiv_bot/blob/master/%E4%BB%95%E7%B5%84%E3%81%BF2.png "サンプル")

# ロゴの引用元
[Logos | Slack Official Digital Assets | Brandfolder](https://brandfolder.com/slack/logos)  
[The Python Logo | Python Software Foundation](https://www.python.org/community/logos/)
