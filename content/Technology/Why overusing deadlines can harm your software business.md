Title: Why overusing deadlines can harm your software business
Date: 2020-08-20 22:55
Slug: overuse-deadlines-harm-software
Tags: software, deadlines, harm, business, overuse, technical debt, quality
Category: Technology
Status: published

In software projects, we often arbitrarily set deadlines without proper justification. Used like that, they are detrimental to your software business and your employees. Before you jump at my throat, I am not against having a project schedule, milestones, or project management in general. It’s a matter of mindset, language, and making conscious trade-offs. I’m also not against deadlines entirely. I merely think that they are overused, with little conscious thought and justification, and with no regard to the consequences.

![Clocks][lucian-alexe-f2xftov0p9y-unsplash]

Photo by [Lucian Alexe](https://unsplash.com/@lucian_alexe?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/clocks?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

# Language matters

If you call a date a deadline, then that implies that you have set it in stone, it is inflexible. You are making the constraint of time the foremost priority implicitly. If there is no clear, highly defined, and communicated motivation behind it, then it is likely to breed resentment and discontent in many of your employees. And by that, I don’t mean some meaningless management jargon like: to meet our business objectives. That may be so, but it needs to be more specific than that.

- Which objective does it aim to impact, and in what measure?
- What kind of trade-offs are you willing to take to meet that objective?
- What is the cost of delay?

Such a deadline example would be: a country in which we operate is introducing new laws and regulations, and we have until date X to comply with them.

I’ve mentioned the time constraint already. The main ones that you can control in a project are time, cost, scope, and quality. If you have a deadline and it’s not something that you know well ahead of time, then your time is fixed, and you will need to sacrifice either cost, scope, or quality. But if you always consider time like that, then it is likely that you are fixated on every other constraint as well. What happens often is that quality is sacrificed implicitly first, with disastrous medium to long term results. Quality is not even acknowledged explicitly as a constraint by many project managers.

I would suggest that you sacrifice quality last. Make sure that the project has adequate staff. You can add more people to the project by increasing budget/costs, and this will gain you time. But this needs to be done as early as possible because trying to do this very late will backfire as you can read in [The Mythical Man-Month](https://en.wikipedia.org/wiki/The_Mythical_Man-Month). Reduce scope as much as possible, and if that reached its limits, then you will be forced to sacrifice on quality if time is indeed the foremost priority.

# The two kinds of quality

When we look at quality, there are two kinds that we need to think about:

- external
- internal

Most non-technical people will understand **external quality** easily because this is what you can see as an end-user.

- Does the application look good?
- Does it do the required functions?
- Does it run without errors?
- Can it handle the load from all the users we have?

Management will understand the danger of sacrificing this kind of quality because it tends to result in immediate negative feedback from the end-users. Yet, even some of this gets sacrificed more often than we’d like to admit if we fixate on the time constraint.

**Internal quality,** on the other hand, is more difficult to understand and see, often even for software engineers, especially the inexperienced ones. It represents how easy and safe it is to make future modifications to the application.

- Is the code “clean” and nicely structured?
- Does it have a comprehensive suite of automated tests?
- Is the application’s architecture well designed?

I’m looking at this from a very high-level view here because there are entire books written on each of these questions. [Clean Code](https://www.amazon.com/gp/product/B001GSTOAM/) is one that is usually close at hand for me.

Sacrificing **internal quality** when time could be flexible is a poor financial decision. Financial? Yes, because you are accruing [technical debt](https://en.wikipedia.org/wiki/Technical_debt), which is quite similar to financial debt just less visible. If you don't repay it in short order (by improving the internal quality), then the software will be increasingly more difficult (read: expensive) to modify as time goes on. You will be paying the interest for the technical debt every time you need to add a new feature or fix a bug, and this will slow you down considerably. That means that you need to choose the times when you sacrifice internal quality over time very carefully and deliberately. It also needs to be accompanied by a plan to pay back the technical debt that you've incurred in the short term.

# Software development is a marathon, not a sprint

I’m talking about real and reasonably complicated business software here. It will not get done in one month or three months. Even if you launch the first [minimum viable product](https://en.wikipedia.org/wiki/Minimum_viable_product) to production in 3 months, that is just the beginning. It begins a journey, spanning potentially multiple years in which you continually improve the quality and add new features based on user demand.

Because of this, you need to set a pace that is sustainable in the medium to long term. You cannot just sprint and sprint and sprint again, pushing continuous overtime to keep fixed deadlines. Sustained overtime only gives an illusion of increased productivity anyway, because the per hour quality and quantity of work will inevitably suffer, so you don’t gain much. It can even be entirely counter-productive because overly tired and unfocused engineers will tend to make mistakes that will cost you big time in the long run.

Also, if you sacrifice quality early to meet fixed deadlines, then at first things will move fast, but in a few months, the technical debt will catch up with you, and you will gradually progress slower and slower. You can then throw more resources at the problem, but that will mean ballooning costs to keep up the same pace of development, and you’ll accumulate more technical debt without an explicit focus on internal quality. You need to repay technical debt early and often, and when at all possible, do not accrue significant new debt.

# Having a schedule

When you set a schedule with dates that are not externally imposed, then talk about target dates or milestones. If these are aggressive but not too much so then you can inspire a sense of exciting challenge in your employees, so they will still be taken seriously, and they can rally to meet the challenge. But they know that it’s not a looming sword over their head, the schedule may be extended if there is proper justification for it. Though, you would still want to decrease scope aggressively before resorting to a delay in the target dates. More often than not, this can solve any schedule dependency issues.

Once you have dealt with reducing scope, then instead of sacrificing quality it is better to extend the target date or milestone date until the desired level is satisfied. Investing in quality early actually increases your speed and agility in the medium to long term, so you have much less risk of missing future target dates and milestones, and yes, the eventual deadline. It is a win-win scenario. For this, we do require a specific definition of what that quality entails, but that's a whole other topic. We are not aiming for perfection here because that is entirely impractical, but there should be a well defined, high standard. For many projects, these standards are set far too low.

# Conclusion

Software development is a complex business, and this topic, in particular, is a challenging one. There is a lot more to go into that won’t fit into a single article, but I hope that I have illustrated a few key points:

- overuse of deadlines makes you fixate on the time constraint, so you tend to sacrifice quality
- developing software is a medium to long term investment
- sacrificing quality in the short term will cause you to lose time overall in the medium to long run

How are you using deadlines in your software project?

[lucian-alexe-f2xftov0p9y-unsplash]: {static}/images/lucian-alexe-f2xfTOv0p9Y-unsplash.jpg
