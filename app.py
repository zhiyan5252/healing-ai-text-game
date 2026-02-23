import streamlit as st
  
# ---------------------------
# 0) Page config（必须尽量靠前）
# ---------------------------
st.set_page_config(
    page_title="第一幕 Demo（入口）",
    page_icon="🟣",
    layout="centered",
)

# ---------------------------
# 1) Session init（推荐用 setdefault）
# ---------------------------
 # Session init（推荐用 setdefault）
st.session_state.setdefault("step", 0)
st.session_state.setdefault("emotion_drop_text", "")
st.session_state.setdefault("first_expression", "")
st.session_state.setdefault("dev", True)

st.session_state.setdefault("act2_type", None)
st.session_state.setdefault("act2_branch", None)


# ---------------------------
# 2) Helpers（统一跳转 / 重置 / 文案样式）
# ---------------------------
def goto(n: int):
    st.session_state.step = n
    st.rerun()
 

def next_step():
    st.session_state.step += 1
    st.rerun()

def reset_session():
    st.session_state.step = 0
    st.session_state.emotion_drop_text = ""
    st.session_state.first_expression = ""
    st.rerun()
 

def big_text_block(text: str):
    # 你已经在用这个函数了：保留你的风格
    st.markdown(
        f"""
        <div style="line-height: 1.9; font-size: 18px; white-space: pre-wrap;">
        {text}
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------
# 3) Debug sidebar（可开关）
# ---------------------------
step = st.session_state.step

with st.sidebar:
    st.session_state.dev = st.toggle("开发模式（Debug）", value=st.session_state.dev)

if st.session_state.dev:
    with st.sidebar:
        st.markdown("## Debug")
        st.write("step =", st.session_state.step)
        st.write("drop =", (st.session_state.emotion_drop_text[:20] + "…") if st.session_state.emotion_drop_text else "")
        st.write("expr =", (st.session_state.first_expression[:20] + "…") if st.session_state.first_expression else "")

if st.session_state.dev:
    with st.sidebar:
        st.write("current step:", step)



# ---------------------------
# 4) Main flow（只用 step + goto）
# ---------------------------
step = st.session_state.step

# ======= 动态标题（根据 step 切换） =======

if step <= 6:
    st.title("🟣 第一幕 · 入口")
    st.caption("开屏 → 情绪放置 → 情绪停顿 → 见证 → 托底")
elif step >= 7:
    st.title("🟣 第二幕 · 起步之前")
    st.caption("关于开始、停住，以及不敢继续的那一刻")

st.divider()


# ========== Step 0: 开屏 ==========
if step == 0:
    opening = (
        "我不知道你经历了什么。\n\n"
        "但如果你会来到这里，\n"
        "往往说明你现在\n"
        "需要一点停下来的空间。\n\n"
        "你可以慢慢来。\n"
        "这里不着急。"
    )
    big_text_block(opening)
    st.write("")

    if st.button("继续 →", use_container_width=True):
        goto(1)

# ========== Step 1: 情绪放置区 ==========
elif step == 1:
    s0 = (
        "你不需要马上说清楚。\n\n"
        "如果你愿意，\n"
        "可以先把现在最明显的那种感觉，\n"
        "放在这里。\n\n"
        "不用整理，\n"
        "也不用解释。"
    )
    big_text_block(s0)

    st.write("")
    text = st.text_area(
        "（在这里输入）",
        value=st.session_state.emotion_drop_text,
        height=140,
        placeholder="比如：我有点烦 / 我很乱 / 我说不清楚但很堵……",
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("← 返回", use_container_width=True):
            goto(0)
    with col2:
        if st.button("放下 ➜", use_container_width=True):
            st.session_state.emotion_drop_text = text.strip()
            goto(2)

# ========== Step 2: 情绪停顿区 ==========
elif step == 2:
    s1 = (
        "我看见你已经把它放下了。\n\n"
        "现在，我们可以先停一下。\n\n"
        "接下来发生的事，\n"
        "不会替你判断对错，\n"
        "也不会替你决定方向。"
    )
    big_text_block(s1)

    st.write("")
    if st.session_state.emotion_drop_text:
        with st.expander("你刚才放下的内容（可展开/可不看）"):
            st.write(st.session_state.emotion_drop_text)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("← 返回", use_container_width=True):
            goto(1)
    with col2:
        if st.button("继续 ➜", use_container_width=True):
            goto(3)

# ========== Step 3: 分岔（停在这里 / 继续） ==========
elif step == 3:
    s2 = (
        "接下来我不会安慰你，\n"
        "也不会告诉你该怎么办。\n\n"
        "我能做的，\n"
        "只是陪你直视\n"
        "你正在面对的东西。\n\n"
        "如果你准备好，我们可以继续。\n"
        "如果没有，你可以在这里停下。"
    )
    big_text_block(s2)

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("停在这里", use_container_width=True):
            goto(6)
    with col2:
        if st.button("继续", use_container_width=True):
            goto(4)

# ========== Step 4: 表达区 ==========
elif step == 4:
    s3 = (
        "你可以说一件\n"
        "最近一直困住你的事情。\n\n"
        "不用说完整，\n"
        "也不用说得很清楚。"
    )
    big_text_block(s3)

    st.write("")
    text = st.text_area(
        "（在这里输入）",
        value=st.session_state.first_expression,
        height=160,
        placeholder="比如：我一直在拖延 / 我不知道自己在逃什么 / 我很怕继续下去没结果……",
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("← 返回", use_container_width=True):
            goto(3)
    with col2:
        if st.button("说完了", use_container_width=True):
            st.session_state.first_expression = text.strip()
            goto(5)

# ========== Step 5: 见证回应 ==========
elif step == 5:
    witness_reply = (
        "你说的不是“做不到”，\n"
        "而是“不敢继续”。\n\n"
        "很多时候，\n"
        "真正让人停住的，\n"
        "不是事情本身，\n"
        "而是再次确认努力没有意义的那一刻。"
    )
    big_text_block(witness_reply)

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("我想再说一点", use_container_width=True):
            goto(4)
    with col2:
        if st.button("先停在这里", use_container_width=True):
            goto(6)

# ========== Step 6: 托底结束 ==========
elif step == 6:
    ending_text = (
        "我不会告诉你\n"
        "接下来该怎么走。\n\n"
        "但至少现在，\n"
        "你不需要再\n"
        "一个人承受这些误解。\n\n"
        "你可以带着它们离开，\n"
        "也可以之后再回来。"
    )
    big_text_block(ending_text)

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("结束", use_container_width=True):
         reset_session()


    with col2:
        if st.button("进入第二幕 →", use_container_width=True):
            goto(7)


elif step == 7:
    act2_opening = (
        "如果你愿意，\n"
        "我们可以一起看看——\n"
        "为什么迈出第一步会这么困难，\n"
        "为什么总是停在那一刻，\n"
        "为什么会在继续之前犹豫。"
    )
    big_text_block(act2_opening)

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("← 回到第一幕结尾", use_container_width=True):
            goto(6)

    with col2:
        if st.button("继续 →", use_container_width=True):
            goto(8)  # 先预留 Step8，我们下一步再做

elif step == 8:
    act2_choice = (
        "在继续之前，\n"
        "我想确认一件事。\n\n"
        "你现在卡住的“第一步”，\n"
        "更像下面哪一种？"
    )
    big_text_block(act2_choice)

    st.write("")
    col1, col2, col3 = st.columns(3)

    with col1:
     if st.button("我不知道从哪开始", use_container_width=True):
        st.session_state.act2_type = "confused"
        goto(11)



    with col2:
        if st.button("我知道要做什么，但起不来", use_container_width=True):
            st.session_state.act2_type = "blocked"
            goto(10)

    with col3:
        if st.button("我一开始就想到失败", use_container_width=True):
            st.session_state.act2_type = "hopeless"
            goto(11)

elif step == 9:
    s9 = (
        "很多时候，\n"
        "不是事情太难，\n"
        "也不是能力不够。\n\n"
        "而是——\n"
        "一旦开始，就好像没有回头路了。\n\n"
        "这让人不敢迈出第一步。\n"
        "但你可以停下来，\n"
        "看看自己卡在了哪里。"
    )
    big_text_block(s9)

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("看看自己为什么停住", use_container_width=True):
            goto(10)  # 跳转到 Step10 (后面我们继续完善)  
        

    with col2:
        if st.button("我暂时不想碰这个", use_container_width=True):
            goto(6)  # 可以选择回到托底页面，稍微停顿

    
# =========================
# Step 10: blocked 分支文案（你现在这个版本）
# =========================
elif step == 10:
    s10 = (
        "当你这样看着自己的时候，\n"
        "有些东西可能会慢慢浮现出来。\n\n"
        "它不是一个清晰的想法，\n"
        "更像是一种隐约的预感——\n\n"
        "如果继续下去，\n"
        "也许并不会发生什么改变。\n\n"
        "你不需要立刻对这种预感做出回应。\n"
        "它只是安静地待在那里，\n"
        "让人一时分不清，\n"
        "自己是不是还想再往前一点。"
    )

    big_text_block(s10)

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("再靠近一点", use_container_width=True):
            # 这里我们统一进入 Step11
            # Step11 会根据 act2_type 决定显示哪一段
            goto(11)

    with col2:
        if st.button("到这里就好", use_container_width=True):
            goto(6)  # 回到第一幕托底结束（你现在的设计）

elif step == 10:  # Confused 分支
    s10 = (
        "你知道该做什么，\n"
        "可总是停在原地。\n\n"
        "你知道继续做下去，\n"
        "会让一切变得更好，\n"
        "可就是无法开始。\n\n"
        "这不是懒惰，不是缺乏能力。\n"
        "它是一种停不下来的循环，\n"
        "你一直在想要迈出那一步，\n"
        "但每次都停在了想的地方。\n\n"
        "有时，我们会等到最完美的时机，\n"
        "但也许，最完美的时机，\n"
        "就是现在。\n\n"
        "你可以选择继续，\n"
        "或者先停下来，给自己更多空间，\n"
        "让这一步成为你最轻松的一步。"
    )
    big_text_block(s10)

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("继续尝试", use_container_width=True):
            goto(11)  # 继续进入 Step11

    with col2:
        if st.button("先停下来", use_container_width=True):
            goto(6)   # 回到托底


# =========================
# Step 11: 分支解释页（先把 confused 写完整，另外两个先给占位）
# =========================
elif step == 11:
    # 保险：如果用户没经过 Step8，给个默认值，避免 None 报错
    act2_type = st.session_state.get("act2_type", "confused")

    if act2_type == "confused":
        s11 = (
            "有时候，\n"
            "「不知道从哪开始」\n"
            "并不是因为你什么都不懂。\n\n"
            "而是因为你站在原地的时候，\n"
            "看到的不是一步，\n"
            "而是背后的一整条路。\n\n"
            "你可能在想：\n"
            "第一步是不是就意味着要走到底？\n"
            "是不是一旦开始，\n"
            "就不能再回头了？\n\n"
            "所以你停在这里，\n"
            "不是因为你没准备好，\n"
            "而是因为你不想走错第一步。"
        )

        big_text_block(s11)

        st.write("")
        col1, col2 = st.columns(2)

        with col1:
            # 这里我们先把“下一步”统一跳到 Step12（你后面要做的内容）
            if st.button("一起看看，第一步其实是什么", use_container_width=True):
                st.session_state.act2_branch = "redefine_first_step"
                goto(12)

        with col2:
            if st.button("先停在这里", use_container_width=True):
                goto(6)

    elif act2_type == "blocked":
        s11 = (
            "你卡住的地方，\n"
            "更像是「知道要做什么」，\n"
            "却总是难以启动。\n\n"
            "很多时候，\n"
            "挡住你的不是懒，\n"
            "也不是能力。\n"
            "而是那种——\n"
            "一旦开始，就得面对结果的压力。"
        )
        big_text_block(s11)

        st.write("")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("继续往下看", use_container_width=True):
                st.session_state.act2_branch = "start_pressure"
                goto(12)
        with col2:
            if st.button("先停在这里", use_container_width=True):
                goto(6)

    elif act2_type == "hopeless":
        s11 = (
            "你说的那个感觉，\n"
            "更像是「一开始就觉得会失败」。\n\n"
            "于是开始这件事，\n"
            "就不再只是一个动作，\n"
            "而像是在把自己推向一次可能的否定。\n\n"
            "所以你不是不想做，\n"
            "而是不想再经历一次“努力也没用”。"
        )
        big_text_block(s11)

        st.write("")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("继续往下看", use_container_width=True):
                st.session_state.act2_branch = "fear_of_invalid_effort"
                goto(12)
        with col2:
            if st.button("先停在这里", use_container_width=True):
                goto(6)

    else:
        # 万一 act2_type 被写成别的值
        big_text_block("这一页暂时找不到对应的分支。我们先回到选择页。")
        st.write("")
        if st.button("返回选择", use_container_width=True):
            goto(8)
 
elif step == 12:
    s12 = (
        "也许你担心的，\n"
        "并不是“这一步该怎么走”。\n\n"
        "而是——\n"
        "一旦走出去，\n"
        "就再也不能停下来。\n\n"
        "但这里的第一步，\n"
        "并不是承诺，\n"
        "也不是开始一段必须完成的路。\n\n"
        "它只是一个很小的动作，\n"
        "小到你随时可以收回。\n"
        "小到它什么也不代表。\n\n"
        "你只是在确认一件事：\n"
        "「这一步，本身会不会出事。」"
    )
    big_text_block(s12)

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("试试这个第一步", use_container_width=True):
            goto(13)  # 下一步再设计

    with col2:
        if st.button("先记住这一点", use_container_width=True):
            goto(6)   # 或回到托底 / 结束

elif step == 13:
    s13 = (
        "你已经做到了第一步。\n\n"
        "但也许，“第一步”并不是你以为的那样。\n\n"
        "它不需要承诺，也不需要确定方向。\n\n"
        "有时候，开始的意思只是：\n"
        "你愿意试一下，不一定要走完这一整条路。\n\n"
        "你可以继续试试，或者退回来，再决定。\n\n"
        "如果你愿意，\n"
        "你可以给自己一个轻松的开始。\n\n"
        "它没有错，\n"
        "只是一个你能控制的开始。"
    )
    big_text_block(s13)

    st.write("")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("继续尝试", use_container_width=True):
            goto(14)  # 继续前往下一步或 Blocked/Hopeless 分支

    with col2:
        if st.button("先停下，记住这一点", use_container_width=True):
            goto(6)   # 回到第一幕的托底结束


elif step == 14:
    s14 = (
        "你已经迈出了第一步，\n"
        "不需要马上知道所有的答案，\n"
        "也不需要走得太远。\n\n"
        "如果你准备好了，你可以继续往前走，\n"
        "如果你想停下来，\n"
        "也可以稍微放松一下，给自己时间再考虑下一步。\n\n"
        "重要的不是速度，而是你是否愿意走下去。\n"
        "你有时间，也有选择。"
    )
    big_text_block(s14)

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("继续前行", use_container_width=True):
            goto(15)  # 继续进入下一步，去到 Step15 继续引导

    with col2:
        if st.button("暂时放下", use_container_width=True):
            goto(6)   # 停下来，回到第一幕结束


elif step == 15:
    s15 = (
        "第一小步，\n"
        "并不是为了给你一个答案，而是为了让你看见这一刻。\n\n"
        "如果你愿意，你可以继续往前走，\n"
        "但这一步不会决定你是否能够走到最后。\n\n"
        "有时候，开始并不代表结束，\n"
        "它只代表你开始看到这一切\n"
        "并给自己一个机会，\n"
        "去选择，去体验，去感受。"
    )
    big_text_block(s15)

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("继续探索", use_container_width=True):
            goto(16)  # 继续进入下一步，进入第三幕

    with col2:
        if st.button("稍作停留", use_container_width=True):
            goto(6)   # 回到第一幕，稍作停留，结束当前对话


elif step == 16:  # Blocked 分支
    s16 = (
        "你知道该做什么，\n"
        "可总是停在原地。\n\n"
        "你知道继续做下去，\n"
        "会让一切变得更好，\n"
        "可就是无法开始。\n\n"
        "这不是懒惰，不是缺乏能力。\n"
        "它是一种停不下来的循环，\n"
        "你一直在想要迈出那一步，\n"
        "但每次都停在了想的地方。\n\n"
        "有时，我们会等到最完美的时机，\n"
        "但也许，最完美的时机，\n"
        "就是现在。\n\n"
        "你可以选择继续，\n"
        "或者先停下来，给自己更多空间，\n"
        "让这一步成为你最轻松的一步。"
    )
    big_text_block(s16)

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("继续尝试", use_container_width=True):
            goto(17)  # Step17继续前进

    with col2:
        if st.button("先停下来", use_container_width=True):
            goto(6)   # 回到托底


elif step == 17:  # Hopeless 分支
    s17 = (
        "你没有动力继续，\n"
        "因为你觉得一开始就会失败。\n\n"
        "也许你已经知道，\n"
        "不管做什么，都难以避免结果不如预期。\n\n"
        "你害怕再一次努力，\n"
        "害怕再次面对“没用”的感觉，\n"
        "害怕从一开始就看到失败的结局。\n\n"
        "但不试试，\n"
        "哪来的失败呢？\n\n"
        "每一个开始，\n"
        "都给我们重新选择的机会，\n"
        "即使这一步小到几乎看不见，\n"
        "也依然是你自己的选择。"
    )
    big_text_block(s17)

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("继续尝试", use_container_width=True):
            goto(18)  # 继续深入

    with col2:
        if st.button("先停下来", use_container_width=True):
            goto(6)   # 回到托底




         