import torch
import torch.nn as nn
import torch.nn.functional as F


class UNet(nn.Module):
    def __init__(self, kernel_size=3, padding=1):
        super(UNet, self).__init__()
        self.conv1_1 = nn.Conv2d(1, 32, kernel_size=kernel_size, padding=padding)
        self.conv1_2 = nn.Conv2d(32, 32, kernel_size=kernel_size, padding=padding)
        self.maxpool1 = nn.MaxPool2d(2)

        self.conv2_1 = nn.Conv2d(32, 64, kernel_size=kernel_size, padding=padding)
        self.conv2_2 = nn.Conv2d(64, 64, kernel_size=kernel_size, padding=padding)
        self.maxpool2 = nn.MaxPool2d(2)

        self.conv3_1 = nn.Conv2d(64, 128, kernel_size=kernel_size, padding=padding)
        self.conv3_2 = nn.Conv2d(128, 128, kernel_size=kernel_size, padding=padding)
        self.maxpool3 = nn.MaxPool2d(2)

        self.conv4_1 = nn.Conv2d(128, 256, kernel_size=kernel_size, padding=padding)
        self.conv4_2 = nn.Conv2d(256, 256, kernel_size=kernel_size, padding=padding)
        self.maxpool4 = nn.MaxPool2d(2)

        self.conv5_1 = nn.Conv2d(256, 512, kernel_size=kernel_size, padding=padding)
        self.conv5_2 = nn.Conv2d(512, 512, kernel_size=kernel_size, padding=padding)
        self.conv5_t = nn.ConvTranspose2d(512, 256, 2, stride=2)

        self.conv6_1 = nn.Conv2d(512, 256, kernel_size=kernel_size, padding=padding)
        self.conv6_2 = nn.Conv2d(256, 256, kernel_size=kernel_size, padding=padding)
        self.conv6_t = nn.ConvTranspose2d(256, 128, 2, stride=2)

        self.conv7_1 = nn.Conv2d(256, 128, kernel_size=kernel_size, padding=padding)
        self.conv7_2 = nn.Conv2d(128, 128, kernel_size=kernel_size, padding=padding)
        self.conv7_t = nn.ConvTranspose2d(128, 64, 2, stride=2)

        self.conv8_1 = nn.Conv2d(128, 64, kernel_size=kernel_size, padding=padding)
        self.conv8_2 = nn.Conv2d(64, 64, kernel_size=kernel_size, padding=padding)
        self.conv8_t = nn.ConvTranspose2d(64, 32, 2, stride=2)

        self.conv9_1 = nn.Conv2d(64, 32, kernel_size=kernel_size, padding=padding)
        self.conv9_2 = nn.Conv2d(32, 32, kernel_size=kernel_size, padding=padding)

        self.conv10 = nn.Conv2d(32, 1, kernel_size=kernel_size, padding=padding)

    def forward(self, x):
        conv1 = F.relu(self.conv1_1(x))
        conv1 = F.relu(self.conv1_2(conv1))
        pool1 = self.maxpool1(conv1)

        conv2 = F.relu(self.conv2_1(pool1))
        conv2 = F.relu(self.conv2_2(conv2))
        pool2 = self.maxpool2(conv2)

        conv3 = F.relu(self.conv3_1(pool2))
        conv3 = F.relu(self.conv3_2(conv3))
        pool3 = self.maxpool3(conv3)

        conv4 = F.relu(self.conv4_1(pool3))
        conv4 = F.relu(self.conv4_2(conv4))
        pool4 = self.maxpool4(conv4)

        conv5 = F.relu(self.conv5_1(pool4))
        conv5 = F.relu(self.conv5_2(conv5))

        up6 = torch.cat((self.conv5_t(conv5), conv4), dim=1)
        conv6 = F.relu(self.conv6_1(up6))
        conv6 = F.relu(self.conv6_2(conv6))

        up7 = torch.cat((self.conv6_t(conv6), conv3), dim=1)
        conv7 = F.relu(self.conv7_1(up7))
        conv7 = F.relu(self.conv7_2(conv7))

        up8 = torch.cat((self.conv7_t(conv7), conv2), dim=1)
        conv8 = F.relu(self.conv8_1(up8))
        conv8 = F.relu(self.conv8_2(conv8))

        up9 = torch.cat((self.conv8_t(conv8), conv1), dim=1)
        conv9 = F.relu(self.conv9_1(up9))
        conv9 = F.relu(self.conv9_2(conv9))
        
        out = F.sigmoid(self.conv10(conv9))
        

        return out
