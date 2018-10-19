#include "widget.h"
#include "ui_widget.h"
//************************
int connect_num=0;//产生连接的次数
//************************

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    int port = 5000;
    ui->setupUi(this);
    server.listen(QHostAddress::Any,port);
    connect(&server,&QTcpServer::newConnection,this,&Widget::new_connect);


    ui->lineEdit->setText(get_ip());
    ui->lineEdit_port->setText(QString::number(port));
    setWindowTitle("家居能耗监测系统");


    setMaximumSize(450,450);//设置固定窗口大小
    setMinimumSize(450,450);
}

void Widget::new_connect()
{
    qDebug()<<"有新连接";
    connect_num++;
   // if(connect_num>2)
   //     connect_num=0;
    if(connect_num==1)
    {
        ui->label_state->setText("在线");
        socket=server.nextPendingConnection();//建立握手连接,之后socket会发出readread的信号
    //握手完了之后再还要读，中断的这个连接也要在新连接后做，非常重要
        connect(socket,&QTcpSocket::readyRead,this,&Widget::sockrt_read);
        connect(socket,&QTcpSocket::disconnected,this,&Widget::disconnect);
    }
    else if(connect_num==2)
    {
        ui->label_state_2->setText("在线");
        //下面的话其实还是有点没懂得
        socket_2=server.nextPendingConnection();//建立握手连接,之后socket会发出readread的信号
    //握手完了之后再还要读，中断的这个连接也要在新连接后做，非常重要
        connect(socket_2,&QTcpSocket::readyRead,this,&Widget::sockrt_read_2);
        connect(socket_2,&QTcpSocket::disconnected,this,&Widget::disconnect_2);
    }
 //   else
  //      connect_num = 0;
    else if(connect_num==3)
    {
        ui->label_state_3->setText("在线");
        //下面的话其实还是有点没懂得
        socket_3=server.nextPendingConnection();//建立握手连接,之后socket会发出readread的信号
    //握手完了之后再还要读，中断的这个连接也要在新连接后做，非常重要
        connect(socket_3,&QTcpSocket::readyRead,this,&Widget::sockrt_read_3);
        connect(socket_3,&QTcpSocket::disconnected,this,&Widget::disconnect_3);
    }
    else if(connect_num==4)
    {
        ui->label_state_4->setText("在线");
        //下面的话其实还是有点没懂得
        socket_4=server.nextPendingConnection();//建立握手连接,之后socket会发出readread的信号
    //握手完了之后再还要读，中断的这个连接也要在新连接后做，非常重要
        connect(socket_4,&QTcpSocket::readyRead,this,&Widget::sockrt_read_4);
        connect(socket_4,&QTcpSocket::disconnected,this,&Widget::disconnect_4);
    }
    else if(connect_num==5)
    {
        ui->label_state_5->setText("在线");
        //下面的话其实还是有点没懂得
        socket_5=server.nextPendingConnection();//建立握手连接,之后socket会发出readread的信号
    //握手完了之后再还要读，中断的这个连接也要在新连接后做，非常重要
        connect(socket_5,&QTcpSocket::readyRead,this,&Widget::sockrt_read_5);
        connect(socket_5,&QTcpSocket::disconnected,this,&Widget::disconnect_5);
    }
    else if(connect_num==6)
    {
        ui->label_state_6->setText("在线");
        //下面的话其实还是有点没懂得
        socket_6=server.nextPendingConnection();//建立握手连接,之后socket会发出readread的信号
    //握手完了之后再还要读，中断的这个连接也要在新连接后做，非常重要
        connect(socket_6,&QTcpSocket::readyRead,this,&Widget::sockrt_read_6);
        connect(socket_6,&QTcpSocket::disconnected,this,&Widget::disconnect_6);
    }
}

void Widget::disconnect()
{
    qDebug()<<"1_中断";
    ui->label_state->setText("中断");
    ui->lineEdit_current->clear();
    ui->lineEdit_volot->clear();
    ui->lineEdit_kwh->clear();
    connect_num--;
}

void Widget::disconnect_2()
{
    qDebug()<<"2_中断";
    ui->label_state_2->setText("中断");
    ui->lineEdit_current_2->clear();
    ui->lineEdit_volot_2->clear();
    ui->lineEdit_kwh_2->clear();
    connect_num--;
}

void Widget::disconnect_3()
{
    qDebug()<<"3_中断";
    ui->label_state_3->setText("中断");
    ui->lineEdit_current_3->clear();
    ui->lineEdit_volot_3->clear();
    ui->lineEdit_kwh_3->clear();
    connect_num--;
}
void Widget::disconnect_4()
{
    qDebug()<<"4_中断";
    ui->label_state_4->setText("中断");
    ui->lineEdit_current_4->clear();
    ui->lineEdit_volot_4->clear();
    ui->lineEdit_kwh_4->clear();
    connect_num--;
}
void Widget::disconnect_5()
{
    qDebug()<<"5_中断";
    ui->label_state_5->setText("中断");
    ui->lineEdit_current_5->clear();
    ui->lineEdit_volot_5->clear();
    ui->lineEdit_kwh_5->clear();
    connect_num--;
}
void Widget::disconnect_6()
{
    qDebug()<<"6_中断";
    ui->label_state_6->setText("中断");
    ui->lineEdit_current_6->clear();
    ui->lineEdit_volot_6->clear();
    ui->lineEdit_kwh_6->clear();
    connect_num--;
}
QString  Widget::get_ip()//获取本地ip方法
{   //下面这句话的意思不知道，大概是把数据都放到链表里
    QList<QHostAddress> list = QNetworkInterface::allAddresses();
    foreach (QHostAddress address, list)
        {
          // if(address.protocol() == QAbstractSocket::IPv4Protocol)
            //查找需要的IP
           if(address.toString().mid(0,7)=="192.168")
           {
               qDebug()<<address.toString();
               return address.toString();
           }
           //return address.toString();
        }
           return 0;
}
void  Widget::sockrt_read()//读取一号数据
{
    QString str_1;
    QString str_2;
    QString str_3;
    QString str;
    QByteArray buffer;
    buffer = socket->readAll();
    qDebug()<<"端口1："<<buffer;
    str = buffer;//为何不能直接在这里去除空格
    str_1 = str.remove(QRegExp("\\s")).mid(34,4);//电流
    str_2 = str.remove(QRegExp("\\s")).mid(29,3);//电压
    str_3 = str.remove(QRegExp("\\s")).mid(25,4);//电能
    ui->lineEdit_current->setText(str_1);
    ui->lineEdit_volot->setText(str_2);
    ui->lineEdit_kwh->setText(str_3);
 //   qDebug()<<"数据："<<str.toUtf8();
}

void  Widget::sockrt_read_2()//读取二号数据
{
    QString str_1;
    QString str_2;
    QString str_3;
    QString str;
    QByteArray buffer;
    buffer = socket_2->readAll();
    qDebug()<<"端口2："<<buffer;
    str = buffer;//为何不能直接在这里去除空格
    str_1 = str.remove(QRegExp("\\s")).mid(34,4);
    str_2 = str.remove(QRegExp("\\s")).mid(29,3);
    str_3 = str.remove(QRegExp("\\s")).mid(25,4);
    ui->lineEdit_current_2->setText(str_1);
    ui->lineEdit_volot_2->setText(str_2);
    ui->lineEdit_kwh_2->setText(str_3);
}

void  Widget::sockrt_read_3()//读取二号数据
{
    QString str_1;
    QString str_2;
    QString str_3;
    QString str;
    QByteArray buffer;
    buffer = socket_3->readAll();
    qDebug()<<"端口3："<<buffer;
    str = buffer;//为何不能直接在这里去除空格
    str_1 = str.remove(QRegExp("\\s")).mid(34,4);
    str_2 = str.remove(QRegExp("\\s")).mid(29,3);
    str_3 = str.remove(QRegExp("\\s")).mid(25,4);
    ui->lineEdit_current_3->setText(str_1);
    ui->lineEdit_volot_3->setText(str_2);
    ui->lineEdit_kwh_3->setText(str_3);
}
void  Widget::sockrt_read_4()//读取二号数据
{
    QString str_1;
    QString str_2;
    QString str_3;
    QString str;
    QByteArray buffer;
    buffer = socket_4->readAll();
    qDebug()<<"端口4："<<buffer;
    str = buffer;//为何不能直接在这里去除空格
    str_1 = str.remove(QRegExp("\\s")).mid(34,4);
    str_2 = str.remove(QRegExp("\\s")).mid(29,3);
    str_3 = str.remove(QRegExp("\\s")).mid(25,4);
    ui->lineEdit_current_4->setText(str_1);
    ui->lineEdit_volot_4->setText(str_2);
    ui->lineEdit_kwh_4->setText(str_3);
}
void  Widget::sockrt_read_5()//读取二号数据
{
    QString str_1;
    QString str_2;
    QString str_3;
    QString str;
    QByteArray buffer;
    buffer = socket_5->readAll();
    qDebug()<<"端口5："<<buffer;
    str = buffer;//为何不能直接在这里去除空格
    str_1 = str.remove(QRegExp("\\s")).mid(34,4);
    str_2 = str.remove(QRegExp("\\s")).mid(29,3);
    str_3 = str.remove(QRegExp("\\s")).mid(25,4);
    ui->lineEdit_current_5->setText(str_1);
    ui->lineEdit_volot_5->setText(str_2);
    ui->lineEdit_kwh_5->setText(str_3);
}
void  Widget::sockrt_read_6()//读取二号数据
{
    QString str_1;
    QString str_2;
    QString str_3;
    QString str;
    QByteArray buffer;
    buffer = socket_6->readAll();
    qDebug()<<"端口6："<<buffer;
    str = buffer;//为何不能直接在这里去除空格
    str_1 = str.remove(QRegExp("\\s")).mid(34,4);
    str_2 = str.remove(QRegExp("\\s")).mid(29,3);
    str_3 = str.remove(QRegExp("\\s")).mid(25,4);
    ui->lineEdit_current_6->setText(str_1);
    ui->lineEdit_volot_6->setText(str_2);
    ui->lineEdit_kwh_6->setText(str_3);
}
Widget::~Widget()
{
    delete ui;
}
