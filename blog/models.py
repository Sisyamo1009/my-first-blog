#models.py

# モジュールインポート
from django.db import models
from django.utils import timezone

# テーブル：Post（ブログポスト）
# カラム：author（著者）          …auth.Userの外部キー
#         title（タイトル） 　    …200文字制限付きテキスト
#         text（本文）            …制限無しテキスト
#         created_date（作成日）  …デフォルトは現在時刻
#         published_date（公開日）…NULL許容
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # 公開ボタンが押下された場合、公開日に現在時刻を設定する
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # 承認されたコメントのみを取得
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    
    # タイトルを返す
    def __str__(self):
        return self.title

# テーブル：Comment（コメント）
# カラム：post（ブログポスト）          …blog.Postの外部キー
#         author（登録者）              …200文字制限付きテキスト
#         text（コメント本文）          …制限無しテキスト
#         created_date（作成日）        …デフォルトは現在時刻
#         approved_comment（承認フラグ）…Bool型（デフォルトはFalse）
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    # 承認処理
    def approve(self):
        self.approved_comment = True
        self.save()

    # 本文を返す
    def __str__(self):
        return self.text