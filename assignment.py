{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled43.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNCcKBrDdXZ+8A8cydhLDpS",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/OnurKor/C8132-Onur-python-assignment/blob/main/assignment.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SDrc3Mogq5Cu"
      },
      "source": [
        ""
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y7lvyHA4r5JX",
        "outputId": "d720ea7f-2129-4c53-b2af-9c371102db03"
      },
      "source": [
        "age = input(\"Are you a cigarette addict older than 75 years old? (Only Yes or No) \").title().strip()\n",
        "chronic = input(\"Do you have a severe chronic disease? (Only Yes or No) \").title().strip()\n",
        "immune = input(\"Is your immune system too weak? (Only Yes or No) \").title().strip()\n",
        "risk = (age == \"Yes\") or (chronic == \"Yes\") or (immune == \"Yes\")\n",
        "if risk:\n",
        "  print(\"You are in risky group\")\n",
        "else :\n",
        "  print( \"You are not in risky group\")\n",
        "  \n"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Are you a cigarette addict older than 75 years old? (Only Yes or No) yes\n",
            "Do you have a severe chronic disease? (Only Yes or No) yes\n",
            "Is your immune system too weak? (Only Yes or No) yes\n",
            "You are in risky group\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nXu75j7suki-"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}