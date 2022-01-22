.class public Lorg/knightsquad/droidflag/MainActivity;
.super Landroidx/appcompat/app/AppCompatActivity;
.source "MainActivity.java"


# instance fields
.field private inputFlagET:Landroid/widget/EditText;

.field private kctfTitle:Landroid/widget/TextView;

.field private validateButton:Landroid/widget/Button;


# direct methods
.method public constructor <init>()V
    .locals 0

    .line 13
    invoke-direct {p0}, Landroidx/appcompat/app/AppCompatActivity;-><init>()V

    return-void
.end method

.method static synthetic access$000(Lorg/knightsquad/droidflag/MainActivity;)Landroid/widget/EditText;
    .locals 0

    .line 13
    iget-object p0, p0, Lorg/knightsquad/droidflag/MainActivity;->inputFlagET:Landroid/widget/EditText;

    return-object p0
.end method


# virtual methods
.method protected onCreate(Landroid/os/Bundle;)V
    .locals 1

    .line 20
    invoke-super {p0, p1}, Landroidx/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    const p1, 0x7f0c001c

    .line 21
    invoke-virtual {p0, p1}, Lorg/knightsquad/droidflag/MainActivity;->setContentView(I)V

    const p1, 0x7f0900c5

    .line 23
    invoke-virtual {p0, p1}, Lorg/knightsquad/droidflag/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Landroid/widget/TextView;

    iput-object p1, p0, Lorg/knightsquad/droidflag/MainActivity;->kctfTitle:Landroid/widget/TextView;

    const-string v0, "|| KnightCTF 2022 || Organized by Knight Squad ||"

    .line 24
    invoke-virtual {p1, v0}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    .line 25
    iget-object p1, p0, Lorg/knightsquad/droidflag/MainActivity;->kctfTitle:Landroid/widget/TextView;

    const/4 v0, 0x1

    invoke-virtual {p1, v0}, Landroid/widget/TextView;->setSelected(Z)V

    const p1, 0x7f0900be

    .line 27
    invoke-virtual {p0, p1}, Lorg/knightsquad/droidflag/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Landroid/widget/EditText;

    iput-object p1, p0, Lorg/knightsquad/droidflag/MainActivity;->inputFlagET:Landroid/widget/EditText;

    const p1, 0x7f09005f

    .line 28
    invoke-virtual {p0, p1}, Lorg/knightsquad/droidflag/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Landroid/widget/Button;

    iput-object p1, p0, Lorg/knightsquad/droidflag/MainActivity;->validateButton:Landroid/widget/Button;

    .line 30
    new-instance v0, Lorg/knightsquad/droidflag/MainActivity$1;

    invoke-direct {v0, p0}, Lorg/knightsquad/droidflag/MainActivity$1;-><init>(Lorg/knightsquad/droidflag/MainActivity;)V

    invoke-virtual {p1, v0}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    return-void
.end method
