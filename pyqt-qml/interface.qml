import QtQuick 1.0

Rectangle {
    signal getTime;

    anchors.fill: parent
    color: "black"

    function updateMessage(text) {
        messageText.text = text;
    }

    Text {
        id: messageText
        anchors.centerIn: parent; color: "white"
    }

    MouseArea {
        anchors.fill: parent
        onClicked: getTime()
    }
}
