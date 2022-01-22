.class Lorg/knightsquad/droidflag/MainActivity$1;
.super Ljava/lang/Object;
.source "MainActivity.java"

# interfaces
.implements Landroid/view/View$OnClickListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lorg/knightsquad/droidflag/MainActivity;->onCreate(Landroid/os/Bundle;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lorg/knightsquad/droidflag/MainActivity;


# direct methods
.method constructor <init>(Lorg/knightsquad/droidflag/MainActivity;)V
    .locals 0

    .line 30
    iput-object p1, p0, Lorg/knightsquad/droidflag/MainActivity$1;->this$0:Lorg/knightsquad/droidflag/MainActivity;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 4

    .line 34
    iget-object p1, p0, Lorg/knightsquad/droidflag/MainActivity$1;->this$0:Lorg/knightsquad/droidflag/MainActivity;

    invoke-static {p1}, Lorg/knightsquad/droidflag/MainActivity;->access$000(Lorg/knightsquad/droidflag/MainActivity;)Landroid/widget/EditText;

    move-result-object p1

    invoke-virtual {p1}, Landroid/widget/EditText;->getText()Landroid/text/Editable;

    move-result-object p1

    invoke-virtual {p1}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object p1

    .line 35
    invoke-virtual {p1}, Ljava/lang/String;->isEmpty()Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    .line 36
    iget-object p1, p0, Lorg/knightsquad/droidflag/MainActivity$1;->this$0:Lorg/knightsquad/droidflag/MainActivity;

    const-string v0, "Please enter a flag"

    invoke-static {p1, v0, v1}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object p1

    invoke-virtual {p1}, Landroid/widget/Toast;->show()V

    goto/16 :goto_0

    .line 37
    :cond_0
    invoke-virtual {p1}, Ljava/lang/String;->length()I

    move-result v0

    const/16 v2, 0xa

    if-gt v0, v2, :cond_1

    .line 38
    iget-object p1, p0, Lorg/knightsquad/droidflag/MainActivity$1;->this$0:Lorg/knightsquad/droidflag/MainActivity;

    sget-object v0, Lorg/knightsquad/droidflag/KnightCTF;->flag:Ljava/lang/String;

    invoke-static {p1, v0, v1}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object p1

    invoke-virtual {p1}, Landroid/widget/Toast;->show()V

    goto/16 :goto_0

    .line 40
    :cond_1
    new-instance v0, Lorg/knightsquad/droidflag/StringHandler;

    invoke-direct {v0}, Lorg/knightsquad/droidflag/StringHandler;-><init>()V

    .line 41
    new-instance v1, Ljava/lang/StringBuilder;

    iget-object v2, p0, Lorg/knightsquad/droidflag/MainActivity$1;->this$0:Lorg/knightsquad/droidflag/MainActivity;

    invoke-virtual {v0, v2}, Lorg/knightsquad/droidflag/StringHandler;->getS1(Landroid/content/Context;)Ljava/lang/String;

    move-result-object v2

    invoke-direct {v1, v2}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    const-string v2, "{"

    .line 42
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    .line 43
    iget-object v2, p0, Lorg/knightsquad/droidflag/MainActivity$1;->this$0:Lorg/knightsquad/droidflag/MainActivity;

    invoke-virtual {v0, v2}, Lorg/knightsquad/droidflag/StringHandler;->getS3(Landroid/content/Context;)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v2, "_"

    .line 44
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    .line 45
    iget-object v3, p0, Lorg/knightsquad/droidflag/MainActivity$1;->this$0:Lorg/knightsquad/droidflag/MainActivity;

    invoke-virtual {v0, v3}, Lorg/knightsquad/droidflag/StringHandler;->getS2(Landroid/content/Context;)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    .line 46
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    .line 47
    iget-object v2, p0, Lorg/knightsquad/droidflag/MainActivity$1;->this$0:Lorg/knightsquad/droidflag/MainActivity;

    invoke-virtual {v0, v2}, Lorg/knightsquad/droidflag/StringHandler;->getS4(Landroid/content/Context;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v0, "}"

    .line 48
    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    .line 49
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v0, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result p1

    const/high16 v0, 0x7f100000

    if-eqz p1, :cond_2

    .line 50
    new-instance p1, Landroidx/appcompat/app/AlertDialog$Builder;

    iget-object v1, p0, Lorg/knightsquad/droidflag/MainActivity$1;->this$0:Lorg/knightsquad/droidflag/MainActivity;

    invoke-direct {p1, v1, v0}, Landroidx/appcompat/app/AlertDialog$Builder;-><init>(Landroid/content/Context;I)V

    .line 51
    iget-object v0, p0, Lorg/knightsquad/droidflag/MainActivity$1;->this$0:Lorg/knightsquad/droidflag/MainActivity;

    invoke-virtual {v0}, Lorg/knightsquad/droidflag/MainActivity;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const v1, 0x7f0f006d

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p1, v0}, Landroidx/appcompat/app/AlertDialog$Builder;->setTitle(Ljava/lang/CharSequence;)Landroidx/appcompat/app/AlertDialog$Builder;

    .line 52
    iget-object v0, p0, Lorg/knightsquad/droidflag/MainActivity$1;->this$0:Lorg/knightsquad/droidflag/MainActivity;

    invoke-virtual {v0}, Lorg/knightsquad/droidflag/MainActivity;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const v1, 0x7f0f0063

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p1, v0}, Landroidx/appcompat/app/AlertDialog$Builder;->setMessage(Ljava/lang/CharSequence;)Landroidx/appcompat/app/AlertDialog$Builder;

    .line 53
    invoke-virtual {p1}, Landroidx/appcompat/app/AlertDialog$Builder;->show()Landroidx/appcompat/app/AlertDialog;

    goto :goto_0

    .line 55
    :cond_2
    new-instance p1, Landroidx/appcompat/app/AlertDialog$Builder;

    iget-object v1, p0, Lorg/knightsquad/droidflag/MainActivity$1;->this$0:Lorg/knightsquad/droidflag/MainActivity;

    invoke-direct {p1, v1, v0}, Landroidx/appcompat/app/AlertDialog$Builder;-><init>(Landroid/content/Context;I)V

    .line 56
    iget-object v0, p0, Lorg/knightsquad/droidflag/MainActivity$1;->this$0:Lorg/knightsquad/droidflag/MainActivity;

    invoke-virtual {v0}, Lorg/knightsquad/droidflag/MainActivity;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const v1, 0x7f0f0064

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p1, v0}, Landroidx/appcompat/app/AlertDialog$Builder;->setTitle(Ljava/lang/CharSequence;)Landroidx/appcompat/app/AlertDialog$Builder;

    .line 57
    iget-object v0, p0, Lorg/knightsquad/droidflag/MainActivity$1;->this$0:Lorg/knightsquad/droidflag/MainActivity;

    invoke-virtual {v0}, Lorg/knightsquad/droidflag/MainActivity;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const v1, 0x7f0f0065

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p1, v0}, Landroidx/appcompat/app/AlertDialog$Builder;->setMessage(Ljava/lang/CharSequence;)Landroidx/appcompat/app/AlertDialog$Builder;

    .line 58
    invoke-virtual {p1}, Landroidx/appcompat/app/AlertDialog$Builder;->show()Landroidx/appcompat/app/AlertDialog;

    :goto_0
    return-void
.end method
