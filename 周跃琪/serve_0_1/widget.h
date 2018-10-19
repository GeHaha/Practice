#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QTcpServer>
#include <QTcpSocket>
#include <QNetworkInterface>
#include <QDebug>

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = 0);
    ~Widget();
    void new_connect();
    QString get_ip();

    void sockrt_read();
    void disconnect();

    void sockrt_read_2();
    void disconnect_2();

    void sockrt_read_3();
    void disconnect_3();

    void sockrt_read_4();
    void disconnect_4();

    void sockrt_read_5();
    void disconnect_5();

    void sockrt_read_6();
    void disconnect_6();

private:
    Ui::Widget *ui;
    QTcpSocket* socket;//这个socket最好是用指针型的为好
    QTcpSocket* socket_2;
    QTcpSocket* socket_3;
    QTcpSocket* socket_4;
    QTcpSocket* socket_5;
    QTcpSocket* socket_6;
    QTcpServer server;

};

#endif // WIDGET_H
