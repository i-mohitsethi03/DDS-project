🐍 Python Mini-Projects Collection

This repository contains a collection of Python command-line projects, each designed to demonstrate fundamental programming concepts and the use of core data structures.

1) 🧮 Expression Calculator
📌 Overview

A command-line Expression Calculator that evaluates infix mathematical expressions. It uses the Shunting-yard algorithm to convert infix expressions into postfix (RPN), and then evaluates them while handling operator precedence and parentheses.

🔑 Features

🔄 Infix → Postfix conversion (Shunting-yard algorithm).

🧮 Postfix evaluation using a stack.

🥇 Operator precedence handled (*, / before +, -).

🧠 Parentheses support for grouping.

⚠️ Error handling: mismatched parentheses, division by zero, invalid input.

🔢 Supports integers and floating-point numbers.

🛠️ Concepts & Data Structures

Stack (list) → for operators and operands.

Shunting-yard algorithm → infix → postfix.

Stack evaluation → compute postfix expression.

2) 📚 E-Library Book Management
📌 Overview

A simple E-Library Management System to borrow and return books. It maintains an inventory using a linked list and supports an undo feature using a stack, so recent borrow/return actions can be reverted.

🔑 Features

📖 Borrow Books → mark as borrowed if available.

🔄 Return Books → add back to the inventory.

↩️ Undo Actions → undo the most recent borrow/return.

🔍 Search & Filter → by title or author.

📊 Display Inventory → shows availability of all books

🛠️ Concepts & Data Structures

Linked List → stores book inventory.

Stack (list) → stores recent actions for undo.

Search/filter → title/author lookup.

3) 💬 Chat Message History Manager
📌 Overview

A command-line Chat Message History Manager that simulates storing, undoing, and redoing sent messages. It uses a queue for managing incoming messages and a stack for undo/redo actions, with timestamp tracking for each message.

🔑 Features

📥 Store Messages → add to message queue with timestamps.

↩️ Undo Last Sent Message → move it to the undo stack.

🔁 Redo Last Action → re-send undone messages.

⏱️ Timestamp Tracking → each message is logged with time sent.

📜 View Message History → displays all messages in order.

🛠️ Concepts & Data Structures

Queue (collections.deque) → for incoming messages.

Stack (list) → for undo/redo functionality.

Datetime module → for timestamps.
