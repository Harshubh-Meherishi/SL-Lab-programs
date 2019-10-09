{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# AgeConvert"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import date \n",
    "  \n",
    "def AgeConvert(birthDate): \n",
    "    today = date.today() \n",
    "    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) \n",
    "  \n",
    "    return age \n",
    "      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22 years\n"
     ]
    }
   ],
   "source": [
    "print(AgeConvert(date(1997, 2, 3)), \"years\") "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# OddRange"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def OddRange(num1, num2):\n",
    "    list1 =list()\n",
    "    for i in range (num1+1,num2-1):\n",
    "        if(i%2!=0):\n",
    "            list1.append(i)\n",
    "    print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]\n"
     ]
    }
   ],
   "source": [
    "OddRange(5,100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.4.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
